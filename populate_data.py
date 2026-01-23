import os
import django
from django.utils import timezone
from datetime import timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from webkato.models import News, NewsCategory, Event, Publication, PublicationCategory, MembershipType

def run():
    print("Cleaning up old data...")
    News.objects.all().delete()
    Event.objects.all().delete()
    Publication.objects.all().delete()
    MembershipType.objects.all().delete()

    print("Creating Categories...")
    cat_method, _ = NewsCategory.objects.get_or_create(name='Методические рекомендации', slug='methods')
    cat_conf, _ = NewsCategory.objects.get_or_create(name='Конференции', slug='conferences')
    cat_edu, _ = NewsCategory.objects.get_or_create(name='Образование', slug='education')

    pub_cat_guideline, _ = PublicationCategory.objects.get_or_create(name='Клинические протоколы', slug='protocols')
    pub_cat_article, _ = PublicationCategory.objects.get_or_create(name='Научные статьи', slug='articles')

    print("Creating News...")
    News.objects.create(
        title='Проведен мастер-класс по артроскопии коленного сустава',
        slug='master-class-arthroscopy-2024',
        category=cat_edu,
        content='В ННЦТО прошел двухдневный мастер-класс с участием ведущих специалистов из Турции. Были разобраны сложные случаи повреждения менисков и передней крестообразной связки. Участники смогли отработать навыки на муляжах и присутствовать на показательных операциях.',
        is_published=True,
        created_at=timezone.now() - timedelta(days=2)
    )
    News.objects.create(
        title='III Съезд травматологов-ортопедов Казахстана',
        slug='iii-congress-kato',
        category=cat_conf,
        content='Съезд собрал более 500 делегатов из 10 стран мира. Основными темами стали инновации в эндопротезировании, лечение политравмы и реабилитация пациентов. В рамках съезда прошла выставка медицинского оборудования.',
        is_published=True,
        created_at=timezone.now() - timedelta(days=10)
    )
    News.objects.create(
        title='Новые методические рекомендации по лечению переломов',
        slug='new-methods-fractures',
        category=cat_method,
        content='Ассоциация выпустила обновленные рекомендации по остеосинтезу длинных трубчатых костей. Документ доступен для скачивания в разделе Публикации для всех членов ассоциации.',
        is_published=True,
        created_at=timezone.now() - timedelta(days=15)
    )

    print("Creating Events...")
    Event.objects.create(
        title='Международная конференция "Травма 2025"',
        slug='trauma-2025',
        date=timezone.now() + timedelta(days=30),
        location='г. Астана, Hotel Rixos',
        description='Ежегодная конференция, посвященная актуальным вопросам современной травматологии. Приглашенные спикеры из Германии, Израиля и России.',
        is_active=True
    )
    Event.objects.create(
        title='Вебинар: "Ошибки при эндопротезировании"',
        slug='webinar-errors-replacement',
        date=timezone.now() + timedelta(days=7),
        location='Онлайн (Zoom)',
        description='Разбор клинических случаев и ошибок при первичном эндопротезировании тазобедренного сустава. Лектор: д.м.н. Бекарисов О.С.',
        is_active=True
    )
    Event.objects.create(
        title='Мастер-класс: Хирургия стопы',
        slug='foot-surgery-masterclass',
        date=timezone.now() + timedelta(days=45),
        location='г. Алматы, ГКБ №4',
        description='Практический курс по коррекции деформаций переднего отдела стопы. Ограниченное количество мест.',
        is_active=True
    )

    print("Creating Publications...")
    Publication.objects.create(
        title='Диагностика и лечение повреждений вращательной манжеты плеча',
        slug='rotator-cuff-guide',
        category=pub_cat_guideline,
        year=2024,
        authors='Батпенов Н.Д., Осипов А.А.',
        description='Клинический протокол, утвержденный МЗ РК. Описывает алгоритмы диагностики и выбора тактики лечения.'
    )
    Publication.objects.create(
        title='Результаты тотального эндопротезирования при диспластическом коксартрозе',
        slug='coxarthrosis-results',
        category=pub_cat_article,
        year=2023,
        authors='Иванов И.И., Петров П.П.',
        description='Анализ 5-летней выживаемости имплантов у пациентов с тяжелой степенью дисплазии.'
    )
    Publication.objects.create(
        title='Применение 3D-печати в ортопедии',
        slug='3d-printing-orthopedy',
        category=pub_cat_article,
        year=2024,
        authors='Сидоров С.С.',
        description='Обзор современных возможностей аддитивных технологий для создания индивидуальных имплантов.'
    )

    print("Creating Membership Types...")
    MembershipType.objects.create(
        name='Стандартное членство',
        slug='standard',
        price=15000.00,
        description='Ежегодный взнос. Дает доступ к библиотеке, скидку 10% на платные мероприятия и право голоса на собраниях.'
    )
    MembershipType.objects.create(
        name='Премиум членство',
        slug='premium',
        price=40000.00,
        description='Включает все привилегии стандарта, плюс бесплатный доступ к 2 мастер-классам в год и приоритетную регистрацию.'
    )
    MembershipType.objects.create(
        name='Студенческое',
        slug='student',
        price=5000.00,
        description='Для резидентов и студентов медицинских ВУЗов. Требуется подтверждение статуса.'
    )

    print("Done! Database populated.")

if __name__ == '__main__':
    run()
