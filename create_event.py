import os
import django
from django.utils import timezone
from datetime import datetime
import pytz

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from webkato.models import Event

# Data extracted
title = "Международная научно-практическая конференция «Междисциплинарная травматология и ортопедия: от диагностики к реабилитации»"
desc = "Посвящена 25-летию Национального Научного центра травматологии и ортопедии им. ак. Н. Батпенова."
date_str = "2026-09-17 09:00"
# Naive datetimes are deprecated, use timezone aware
tz = pytz.timezone('Asia/Almaty')
event_date = tz.localize(datetime.strptime(date_str, "%Y-%m-%d %H:%M"))

# Check if exists to avoid duplicates
event, created = Event.objects.get_or_create(
    slug='conf-2026',
    defaults={
        'title': title,
        'description': desc,
        'date': event_date,
        'location': 'Астана',
        'is_active': True,
        'is_international': True, # It says "International..." in title
        'image': 'events/conf2026.jpg' 
    }
)

if created:
    print(f"Event '{title}' created.")
else:
    print(f"Event '{title}' already exists.")
    # Update fields if needed
    event.title = title
    event.description = desc
    event.date = event_date
    event.image = 'events/conf2026.jpg'
    event.save()
    print("Event updated.")
