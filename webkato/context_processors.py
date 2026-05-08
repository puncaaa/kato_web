from django.conf import settings

def recaptcha_context(request):
    return {
        'RECAPTCHA_SITE_KEY': getattr(settings, 'RECAPTCHA_SITE_KEY', '')
    }
