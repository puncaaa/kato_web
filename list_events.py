import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from webkato.models import Event

def list_events():
    for event in Event.objects.all():
        print(f"Title: {event.title} | Slug: {event.slug}")

if __name__ == "__main__":
    list_events()
