import os
import django
from django.core.files import File
from django.utils.text import slugify
from datetime import datetime
from django.utils.timezone import make_aware

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from webkato.models import Event

e, created = Event.objects.get_or_create(slug='upcoming-scientific-conference-2026', defaults={
    'title': 'Международная научно-практическая конференция',
    'date': make_aware(datetime(2026, 9, 17))
})

e.title = 'Международная научно-практическая конференция «Междисциплинарная травматология и ортопедия: от диагностики к реабилитации»'
e.date_text = '17–18 сентября 2026 года'
e.location = 'Республика Казахстан, г. Астана, Назарбаев Университет, проспект Кабанбай батыра, 53'
e.is_international = True

e.description = """В рамках конференции планируется обсуждение следующих тем:
современные методы диагностики в травматологии и ортопедии
инновационные технологии хирургического лечения
эндопротезирование суставов
травматология крупных суставов и позвоночника
спортивная травматология
ортопедия детского возраста
современные подходы к реабилитации пациентов
междисциплинарные подходы в лечении травм и заболеваний опорно-двигательной системы
новые технологии и медицинские разработки

Участники конференции:
травматологи-ортопеды, хирурги, реабилитологи, научные сотрудники, преподаватели медицинских вузов, молодые ученые и резиденты, специалисты смежных медицинских направлений.

Формат конференции:
пленарные заседания, научные доклады, тематические секции, панельные дискуссии, презентации новых медицинских технологий, обмен международным клиническим опытом.

Организаторы:
Национальный научный центр травматологии и ортопедии имени академика Н. Д. Батпенова
Казахстанская ассоциация травматологов-ортопедов
Академик Нурлан Батпенов атындағы Қоры
Назарбаев Университет"""

e.external_link = 'https://docs.google.com/forms/d/e/1FAIpQLSdwVZQyb7u32EZ55Db0Fj7rZy30MjqNSW_-Vj5zOwe3_3LpvA/viewform'

# The image in the folder
image_path = '/Users/alenpak/Desktop/новая конференция/WhatsApp Image 2026-02-20 at 13.04.23.jpeg' 

if os.path.exists(image_path):
    with open(image_path, 'rb') as f:
        e.image.save('new_conference.jpeg', File(f), save=False)

e.save()

print('Updated conference details successfully.')
