import os
import django
from django.utils.text import slugify

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from webkato.models import News, NewsCategory, Event

def create_news():
    event = Event.objects.filter(slug='conf-2026-astana').first()
    if not event:
        print("Event not found!")
        return

    category = NewsCategory.objects.filter(slug='conferences').first()
    
    # Check if news already exists
    news_slug = 'news-conf-2026-astana'
    news = News.objects.filter(slug=news_slug).first()
    
    if news:
        print("News already exists, updating...")
    else:
        news = News(slug=news_slug)

    news.title = event.title
    news.category = category
    news.content = event.description
    news.is_published = True
    
    # Copy image reference if exists
    if event.image:
        news.image = event.image.name
        
    news.save()
    print(f"News created/updated: {news.title}")

if __name__ == "__main__":
    create_news()
