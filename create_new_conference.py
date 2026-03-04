import os
import django
from django.utils import timezone
from datetime import timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from webkato.models import Event

# The name we infer from the banner image name or context. Let's make it a generic upcoming conference.
# As the image is just a banner, we will set a title and a future date so it appears as upcoming.
# You can customize these later via Django Admin.
title = "Предстоящая научно-практическая конференция"
slug = "upcoming-scientific-conference-2026"
# Set to a future date to show up in the upcoming list and hero slider
date = timezone.now() + timedelta(days=60)
date_text = "Осень 2026 года"
location = "г. Астана"
description = "Приглашаем вас принять участие в нашей новой научно-практической конференции. Подробная информация и программа будут опубликованы позже."
image_path = "events/new_conference_banner.jpeg"

# Check if it already exists to avoid duplicates
if not Event.objects.filter(slug=slug).exists():
    event = Event.objects.create(
        title=title,
        slug=slug,
        date=date,
        date_text=date_text,
        location=location,
        description=description,
        is_active=True,
        is_international=False
    )
    # Assign the image file path relative to MEDIA_ROOT
    event.image.name = image_path
    event.save()
    print(f"Successfully created upcoming event '{title}'")
else:
    print(f"Event with slug '{slug}' already exists.")
