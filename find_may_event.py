import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from webkato.models import Event

# Look for event on May 3
events = [e for e in Event.objects.all() if e.date.month == 5 and e.date.day == 3]
print("Events on May 3:")
for e in events:
    print(f"ID: {e.id}, Title: {e.title}, Date: {e.date}, Slug: {e.slug}")

events_by_text = Event.objects.filter(date_text__icontains="мая")
print("\nEvents with 'мая' in date_text:")
for e in events_by_text:
    print(f"ID: {e.id}, Title: {e.title}, Date: {e.date}, Slug: {e.slug}")
