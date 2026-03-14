import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from webkato.models import Publication

def clear_publications():
    count = Publication.objects.all().count()
    Publication.objects.all().delete()
    print(f"Deleted {count} publications.")

if __name__ == "__main__":
    clear_publications()
