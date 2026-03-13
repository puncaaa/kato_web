import os
import django
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from webkato.models import Event
from django.core.files import File

event = Event.objects.filter(is_active=True).first()
if event:
    print('Found event:', event.title)
    event.date_text = '10-11 сентября 2026 г.'
    
    source_pdf = 'webkato/static/website/img/events/Анонс о конференции 25 лет ННЦТО.pdf'
    if os.path.exists(source_pdf):
        with open(source_pdf, 'rb') as f:
            event.program_pdf.save('anons_2026.pdf', File(f), save=False)
            print('Attached PDF.')
    else:
        print('PDF not found at', source_pdf)
        
    event.save()
    print('Updated event.')
else:
    print('Event not found')
