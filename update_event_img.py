import os
import django
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from webkato.models import Event
from django.core.files import File

event = Event.objects.filter(is_active=True).first()
if event:
    source_img = 'media/events/anons_2026_banner.png'
    if os.path.exists(source_img):
        with open(source_img, 'rb') as f:
            event.image.save('anons_2026_banner.png', File(f), save=False)
            print('Attached new image banner.')
    else:
        print('Image not found at', source_img)
        
    event.save()
    print('Updated event image.')
else:
    print('Event not found')
