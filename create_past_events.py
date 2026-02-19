import os
import django
import pytz
from datetime import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from webkato.models import Event

tz = pytz.timezone('Asia/Almaty')

events = [
    {
        "slug": "conf-2023",
        "title": "XIV Республиканская научно-практическая конференция «Инновации в травматологии и ортопедии»",
        "date": "2023-09-15 09:00",
        "desc": "Обсуждение современных методов лечения и диагностики. Мастер-классы по артроскопии и эндопротезированию.",
        "location": "Астана",
        "is_int": False
    },
    {
        "slug": "conf-2022-turkestan",
        "title": "Научно-практическая конференция в Туркестане",
        "date": "2022-09-20 09:00",
        "desc": "Выездная конференция, посвященная региональным аспектам травматологической помощи.",
        "location": "Туркестан",
        "is_int": False
    },
    {
        "slug": "conf-2021-20th",
        "title": "Юбилейная конференция к 20-летию ННЦТО",
        "date": "2021-09-30 09:00",
        "desc": "Торжественное мероприятие, посвященное 20-летию основания Национального Научного центра травматологии и ортопедии им. академика Н.Д. Батпенова.",
        "location": "Астана",
        "is_int": False
    }
]

for e in events:
    dt = tz.localize(datetime.strptime(e["date"], "%Y-%m-%d %H:%M"))
    obj, created = Event.objects.update_or_create(
        slug=e["slug"],
        defaults={
            'title': e["title"],
            'description': e["desc"],
            'date': dt,
            'location': e["location"],
            'is_international': e["is_int"],
            'is_active': False # Past events
        }
    )
    print(f"Event '{e['title']}' {'created' if created else 'updated'}.")
