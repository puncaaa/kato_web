from django.db import migrations
from django.utils import timezone
import datetime

def add_data(apps, schema_editor):
    News = apps.get_model('webkato', 'News')
    NewsCategory = apps.get_model('webkato', 'NewsCategory')
    Event = apps.get_model('webkato', 'Event')

    # News Categories
    news_cat, _ = NewsCategory.objects.get_or_create(name='Новости', defaults={'slug': 'news'})
    courses_cat, _ = NewsCategory.objects.get_or_create(name='Образовательные курсы', defaults={'slug': 'educational_courses'})

    # 7 items from scraping
    items = [
        # Educational Courses (First two)
        {
            'title': 'Кадаверные курсы в рамках конференции в Караганде',
            'slug': 'cadaver-courses-karaganda-v3',
            'content': 'Уникальная возможность для специалистов! В рамках конференции будут проведены кадаверные курсы от ведущих экспертов России.',
            'image': 'news/rook_1.png',
            'category': courses_cat
        },
        {
            'title': 'AO Trauma Seminar – Основы лечения переломов',
            'slug': 'ao-trauma-seminar-v3',
            'content': 'Семинар AO Trauma посвящён базовым принципам лечения переломов и современным методикам оперативного лечения травм опорно-двигательного аппарата.',
            'image': 'news/rook_2.png',
            'category': courses_cat
        },
        # News (Remaining 5)
        {
            'title': 'Астана принимает мировых лидеров в травматологии',
            'slug': 'astana-congress-rook-v3',
            'content': 'Астана станет центром мирового медицинского сообщества. С 28 по 29 августа 2024 года столица примет IV Съезд травматологов-ортопедов.',
            'image': 'news/rook_3.jpg',
            'category': news_cat
        },
        {
            'title': 'Дата проведения IV Съезда перенесена',
            'slug': 'iv-congress-postponed-v3',
            'content': 'Уважаемые коллеги, информируем вас о том, что дата проведения IV Съезда перенесена на 28-29 августа 2024 года.',
            'image': 'news/rook_4.jpg',
            'category': news_cat
        },
        {
            'title': 'КАТО и Китайская ортопедическая ассоциация подписали меморандум',
            'slug': 'kato-china-memorandum-v3',
            'content': 'Подписан меморандум о сотрудничестве для обмена опытом, проведения совместных исследований и внедрения новых технологий.',
            'image': 'news/rook_5.jpg',
            'category': news_cat
        },
        {
            'title': 'Приглашаем представителей медицинских компаний',
            'slug': 'medical-companies-invitation-v3',
            'content': 'Приглашаем медицинские компании присоединиться к выставке современного оборудования в Назарбаев Университете.',
            'image': 'news/rook_6.jpg',
            'category': news_cat
        },
        {
            'title': 'Директор Фонда Опаль Benoit Dolle посетил ННЦТО',
            'slug': 'benoit-dolle-nncto-v3',
            'content': 'Обсуждались перспективы сотрудничества и работа отделения реабилитации клиники.',
            'image': 'news/rook_7.jpg',
            'category': news_cat
        }
    ]

    for item_data in items:
        News.objects.update_or_create(
            slug=item_data['slug'],
            defaults={
                'title': item_data['title'],
                'content': item_data['content'],
                'image': item_data['image'],
                'category': item_data['category'],
                'is_published': True
            }
        )

    # Karaganda 2025 Event
    # We use aware datetime for Asia/Almaty (UTC+5)
    event_date = timezone.make_aware(datetime.datetime(2025, 10, 9))
    Event.objects.update_or_create(
        slug='karaganda-2025-v3',
        defaults={
            'title': 'Международная научно-практическая конференция «СОВРЕМЕННЫЕ ПОДХОДЫ В ТРАВМАТОЛОГИИ И ОРТОПЕДИИ: ИННОВАЦИИ И ПРАКТИЧЕСКОЕ ПРИМЕНЕНИЕ»',
            'date': event_date,
            'date_text': '9-10 октября 2025 г.',
            'location': 'г. Караганда, Комплекс «ARISTA»',
            'external_link': 'https://conference.nscto.online/',
            'image': 'events/karaganda_poster.png',
            'is_active': False
        }
    )

def remove_data(apps, schema_editor):
    pass

class Migration(migrations.Migration):

    dependencies = [
        ('webkato', '0009_remove_membershipapplication_residence_and_more'),
    ]

    operations = [
        migrations.RunPython(add_data, remove_data),
    ]
