
import os
import django
from django.utils import timezone
from django.utils.text import slugify

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from webkato.models import News, NewsCategory, Event

def create_data():
    # News Categories
    news_cat, _ = NewsCategory.objects.get_or_create(name='Новости', defaults={'slug': 'news'})
    courses_cat, _ = NewsCategory.objects.get_or_create(name='Образовательные курсы', defaults={'slug': 'educational_courses'})

    # Educational Courses (First 2 news from scrape)
    courses = [
        {
            'title': 'Кадаверные курсы в рамках конференции в Караганде',
            'slug': 'cadaver-courses-karaganda',
            'preview': 'В рамках конференции "Современные подходы в травматологии, ортопедии, реабилитации: инновации и практическое применение" будут проведены кадаверные курсы от ведущих экспертов России.',
            'image': 'news/course_1.png'
        },
        {
            'title': 'AO Trauma Seminar – Основы лечения переломов',
            'slug': 'ao-trauma-seminar-fractures',
            'preview': 'Семинар AO Trauma посвящён базовым принципам лечения переломов и современным методикам оперативного лечения травм опорно-двигательного аппарата. Это уникальная возможность для специалистов повысить знания и навыки.',
            'image': 'news/course_2.png'
        }
    ]

    for c in courses:
        News.objects.update_or_create(
            slug=c['slug'],
            defaults={
                'title': c['title'],
                'content': c['preview'],
                'category': courses_cat,
                'image': c['image'],
                'is_published': True
            }
        )

    # News (Other items from scrape)
    news_items = [
        {
            'title': 'Астана принимает мировых лидеров в травматологии: IV Съезд травматологов-ортопедов и III Съезд КАТО',
            'slug': 'astana-congress-2024',
            'preview': 'Астана станет центром мирового медицинского сообщества в области травматологии и ортопедии. С 28 по 29 августа 2024 года столица Казахстана примет IV Съезд травматологов-ортопедов РК.',
            'image': 'news/news_3.jpg'
        },
        {
            'title': 'IV СЪЕЗД ТРАВМАТОЛОГОВ-ОРТОПЕДОВ РК: ДАТА ПЕРЕНЕСЕНА НА 28-29 АВГУСТА 2024 ГОДА',
            'slug': 'iv-congress-postponed',
            'preview': 'Дата проведения IV Съезда травматологов-ортопедов РК и III Съезда Казахстанской ассоциации травматологов-ортопедов перенесена на 28-29 августа 2024 года.',
            'image': 'news/news_4.jpg'
        },
        {
            'title': 'КАТО ПРИНЯТА В СОСТАВ ЕВРОПЕЙСКОЙ ФЕДЕРАЦИИ НАЦИОНАЛЬНЫХ АССОЦИАЦИЙ ОРТОПЕДИИ И ТРАВМАТОЛОГИИ (EFORT)',
            'slug': 'kato-efort-membership',
            'preview': 'Казахстанская ассоциация травматологов и ортопедов (КАТО) официально стала членом Европейской федерации национальных ассоциаций ортопедии и травматологии (EFORT).',
            'image': 'news/news_5.jpg'
        },
        {
            'title': 'Приглашаем представителей медицинских компаний к сотрудничеству в рамках IV Съезда травматологов-ортопедов РК',
            'slug': 'medical-companies-cooperation-2024',
            'preview': 'Приглашаем представителей медицинских компаний принять участие в выставке и выступить спонсорами IV Съезда травматологов-ортопедов РК.',
            'image': 'news/news_6.jpg'
        }
    ]

    for n in news_items:
        News.objects.update_or_create(
            slug=n['slug'],
            defaults={
                'title': n['title'],
                'content': n['preview'],
                'category': news_cat,
                'image': n['image'],
                'is_published': True
            }
        )

    # Karaganda 2025 Event
    Event.objects.update_or_create(
        slug='karaganda-2025',
        defaults={
            'title': 'Международная научно-практическая конференция «СОВРЕМЕННЫЕ ПОДХОДЫ В ТРАВМАТОЛОГИИ И ОРТОПЕДИИ: ИННОВАЦИИ И ПРАКТИЧЕСКОЕ ПРИМЕНЕНИЕ»',
            'date': timezone.datetime(2025, 10, 9, tzinfo=timezone.get_current_timezone()),
            'date_text': '9-10 октября 2025 г.',
            'location': 'г. Караганда, Комплекс «ARISTA»',
            'external_link': 'https://conference.nscto.online/',
            'image': 'events/conference_karaganda_2025.jpg',
            'is_active': False # Past event according to context of adding to past congresses
        }
    )

    print("Data population complete!")

if __name__ == "__main__":
    create_data()
