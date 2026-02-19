import os
import django
import zipfile
import subprocess
import shutil
from pathlib import Path
from django.core.files import File

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from webkato.models import Event
from django.conf import settings

def extract_images():
    print("Starting image extraction...")
    
    events = Event.objects.filter(program_pdf__isnull=False)
    
    for event in events:
        if not event.program_pdf:
            continue
            
        try:
            file_path = event.program_pdf.path
        except ValueError:
            print(f"Skipping {event.title}: File not found on disk/storage.")
            continue
        if not os.path.exists(file_path):
            print(f"File not found: {file_path}")
            continue
            
        # Only process .doc/.docx files
        ext = os.path.splitext(file_path)[1].lower()
        if ext not in ['.doc', '.docx']:
            print(f"Skipping {ext}: {event.title}")
            continue

        print(f"Processing: {event.title} ({ext})")
        
        temp_dir = Path(settings.MEDIA_ROOT) / 'temp_extract'
        os.makedirs(temp_dir, exist_ok=True)
        
        # Strategy: Convert to RTFD (Rich Text with Attachments) which extracts images to a bundle folder
        if ext == '.doc':
            print("  Converting .doc to .rtfd to extract images...")
            rtfd_name = 'converted.rtfd'
            rtfd_path = temp_dir / rtfd_name
            
            try:
                # textutil -convert rtfd source.doc -output target.rtfd
                subprocess.run(['textutil', '-convert', 'rtfd', file_path, '-output', str(rtfd_path)], check=True)
                
                # Check for images inside the rtfd bundle (it's a directory)
                if os.path.exists(rtfd_path) and os.path.isdir(rtfd_path):
                    # List all files in the rtfd directory
                    # Images are usually named like 'pasted-image.tiff', 'image.jpg', etc.
                    # We want to find common image extensions
                    image_extensions = {'.jpg', '.jpeg', '.png', '.tiff', '.bmp'}
                    candidates = []
                    
                    for f in os.listdir(rtfd_path):
                        f_ext = os.path.splitext(f)[1].lower()
                        if f_ext in image_extensions:
                            candidates.append(rtfd_path / f)
                    
                    if not candidates:
                         print("  No images found in RTFD bundle.")
                    else:
                        # Find largest image
                        largest_img_path = max(candidates, key=lambda p: p.stat().st_size)
                        print(f"  Found largest image: {largest_img_path.name} ({largest_img_path.stat().st_size} bytes)")
                        
                        # Save it
                        with open(largest_img_path, 'rb') as img_f:
                            # Convert filename extension if needed/check type? 
                            # Django handles save fine.
                            # Use new name
                            img_filename = f"{event.slug}_extracted{largest_img_path.suffix}"
                            event.image.save(img_filename, File(img_f), save=True)
                            print(f"  Saved image to event: {event.title}")
            except subprocess.CalledProcessError as e:
                 print(f"  RTFD conversion failed: {e}")
            except Exception as e:
                 print(f"  Error during RTFD processing: {e}")

        # Fallback to QuickLook only if no image was saved
        if not event.image:
             # Use qlmanage to generate a preview image of the first page
            print(f"  Generating preview for {file_path} (fallback)...")
            try:
                # qlmanage -t -s 1000 -o <temp_dir> <file_path>
                # It creates <filename>.png in temp_dir
                subprocess.run(['qlmanage', '-t', '-s', '1000', '-o', str(temp_dir), file_path], check=True, stderr=subprocess.DEVNULL)
                
                # Find the generated png
                # qlmanage appends .png to the filename
                preview_filename = os.path.basename(file_path) + '.png'
                preview_path = temp_dir / preview_filename
                
                if os.path.exists(preview_path):
                    print(f"  Generated preview: {preview_path}")
                    with open(preview_path, 'rb') as img_f:
                        # Save as the event image
                        img_name = f"{event.slug}_preview.png"
                        event.image.save(img_name, File(img_f), save=True)
                        print(f"  Saved preview image to event: {event.title}")
                else:
                    print("  Preview file not found after generation.")
            except Exception as e:
                print(f"  Error generating preview: {e}")

        # Cleanup temp dir
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)

    print("Extraction completed.")

if __name__ == '__main__':
    extract_images()
