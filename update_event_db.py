import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from webkato.models import Event

event = Event.objects.filter(is_active=True).first()
if event:
    # Use the image that is currently deployed successfully on the server
    event.image.name = 'events/upcoming_2026_conf.jpeg'
    event.save()
    print('Updated event image to upcoming_2026_conf.jpeg.')
else:
    print('Event not found')
