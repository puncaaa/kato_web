import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from webkato.models import News

def purge_news():
    count = News.objects.all().count()
    News.objects.all().delete()
    print(f"Deleted {count} news items.")

if __name__ == "__main__":
    purge_news()
