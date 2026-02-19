import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from webkato.models import MembershipType

types = [
    {"slug": "local", "name": "Для местных", "price": 10000, "description": "Полный доступ к ресурсам, участие в выборах, скидки на мероприятия."},
    {"slug": "student", "name": "Студенты", "price": 5000, "description": "Для резидентов и докторантов. Доступ к библиотеке, вебинары, гранты."},
    {"slug": "international", "name": "International", "price": 23000, "description": "International Network, Online Access, Event Discounts."},
]

for t in types:
    obj, created = MembershipType.objects.update_or_create(
        slug=t["slug"],
        defaults={"name": t["name"], "price": t["price"], "description": t["description"]}
    )
    print(f"Type '{t['name']}' {'created' if created else 'updated'}.")
