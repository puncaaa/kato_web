import os
import django
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from webkato.models import Event
from django.core.files import File

event = Event.objects.filter(is_active=True).first()
if event:
    source_img = 'webkato/static/website/img/events/new_sliderconf.jpeg'
    if os.path.exists(source_img):
        with open(source_img, 'rb') as f:
            event.image.save('new_sliderconf.jpeg', File(f), save=False)
            print('Attached new designated slider image.')
            
    # Also update external link
    event.external_link = 'https://25yearsnscto.online/ru-RU/nscto26#register'
    event.save()
    print('Updated event.')
else:
    print('Event not found')
