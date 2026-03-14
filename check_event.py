import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from webkato.models import Event

def check_event():
    slug = 'conf-2026-astana'
    event = Event.objects.filter(slug=slug).first()
    if event:
        print(f"ID: {event.id}")
        print(f"Title: {event.title}")
        print(f"Date: {event.date}")
        print(f"Date Text: {event.date_text}")
    else:
        print("Event not found")

if __name__ == "__main__":
    check_event()
