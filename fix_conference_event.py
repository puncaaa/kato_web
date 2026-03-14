import os
import django
from django.utils import timezone
from datetime import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from webkato.models import Event

def fix_conference():
    slug = 'conf-2026-astana'
    event = Event.objects.filter(slug=slug).first()
    
    if not event:
        print("Event not found!")
        return

    # Fix title and date
    event.title = "XIII Международная научно-практическая конференция «Междисциплинарная травматология и ортопедия: от диагностики к реабилитации»"
    # Setting date to 2026-09-10 09:00:00. Almaty is UTC+5, so UTC is 04:00:00
    new_date = datetime(2026, 9, 10, 9, 0, 0)
    event.date = timezone.make_aware(new_date)
    event.date_text = "10-11 сентября 2026 г."
    event.is_international = False # Ensuring it is in local events
    
    event.save()
    print(f"Fixed event: {event.title} | New Date: {event.date}")

if __name__ == "__main__":
    fix_conference()
