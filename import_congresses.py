import os
import django
import shutil
from datetime import datetime
import pytz

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from webkato.models import Event
from django.core.files import File
from django.conf import settings

# Source directory for content
SOURCE_DIR = "/Users/alenpak/Desktop/контент для сайта 3.0"
MEDIA_ROOT = os.path.join(settings.MEDIA_ROOT, 'events', 'archives')

# Ensure target directory exists
os.makedirs(MEDIA_ROOT, exist_ok=True)

tz = pytz.timezone('Asia/Almaty')

# Map filenames to event data
# Format: "filename_part": {data}
# We look for files starting with the year in the source dir
EVENT_DATA = {
    "2011": {
        "slug": "conf-2011-10-years",
        "title": "Научно-практическая конференция, посвященная 10-летию НИИТО",
        "date": "2011-10-01 09:00", 
        "date_text": "Октябрь 2011 г.",
        "location": "Астана",
        "desc": "Юбилейная конференция, посвященная 10-летию НИИ травматологии и ортопедии.",
    },
    "2012": {
        "slug": "conf-2012-petropavlovsk",
        "title": "Научно-практическая конференция в Петропавловске",
        "date": "2012-09-01 09:00", 
        "date_text": "Сентябрь 2012 г.",
        "location": "Петропавловск",
        "desc": "Выездная научно-практическая конференция КАТО в г. Петропавловск.",
    },
    "2013": {
        "slug": "conf-2013-uralsk",
        "title": "Научно-практическая конференция в Уральске",
        "date": "2013-09-01 09:00",
        "date_text": "Сентябрь 2013 г.",
        "location": "Уральск",
        "desc": "Выездная научно-практическая конференция КАТО в г. Уральск.",
    },
    "2021": {
        "slug": "conf-2021-20-years",
        "title": "Юбилейная конференция к 20-летию ННЦТО",
        "date": "2021-09-30 09:00",
        "date_text": "30 сентября 2021 г.",
        "location": "Астана",
        "desc": "Торжественное мероприятие, посвященное 20-летию основания Национального Научного центра травматологии и ортопедии им. академика Н.Д. Батпенова.",
    },
    "2022": {
        "slug": "conf-2022-turkestan",
        "title": "Научно-практическая конференция в Туркестане",
        "date": "2022-09-20 09:00",
        "date_text": "20 сентября 2022 г.",
        "location": "Туркестан",
        "desc": "Выездная конференция, посвященная региональным аспектам травматологической помощи.",
    },
    "2023": {
        "slug": "conf-2023",
        "title": "XIV Республиканская научно-практическая конференция",
        "date": "2023-09-15 09:00",
        "date_text": "15 сентября 2023 г.",
        "location": "Астана",
        "desc": "XIV Республиканская научно-практическая конференция с международным участием.",
    }
}

def import_congresses():
    print("Starting import...")
    
    # 1. Iterate through files in source directory
    for filename in os.listdir(SOURCE_DIR):
        if not (filename.endswith('.pdf') or filename.endswith('.doc') or filename.endswith('.docx')):
            continue
            
        # Check if file starts with a year we know about
        year_prefix = filename[:4]
        if year_prefix in EVENT_DATA:
            data = EVENT_DATA[year_prefix]
            print(f"Processing {year_prefix}: {filename}")
            
            # Create/Update Event
            dt = tz.localize(datetime.strptime(data["date"], "%Y-%m-%d %H:%M"))
            
            event, created = Event.objects.update_or_create(
                slug=data["slug"],
                defaults={
                    'title': data["title"],
                    'description': data["desc"],
                    'date': dt,
                    'date_text': data.get("date_text", ""),
                    'location': data["location"],
                    'is_international': False,
                    'is_active': False # Past event
                }
            )
            
            # Attach file
            source_path = os.path.join(SOURCE_DIR, filename)
            with open(source_path, 'rb') as f:
                # We save it to 'events/programs/' using the model's upload_to
                # Django will handle the file copy
                event.program_pdf.save(filename, File(f), save=True)
                
            print(f"  -> Saved {'new' if created else 'updated'} event: {event.title}")
            print(f"  -> Attached file: {filename}")

    print("Import completed.")

if __name__ == '__main__':
    import_congresses()
