from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType
from .models import News, Event, Publication, PublicationCategory, Comment, MembershipType, MembershipApplication
from .forms import ContactForm, CommentForm, MembershipApplicationForm, UserRegistrationForm
from django.contrib.auth import logout
from django.http import HttpResponseNotAllowed
from django.core.mail import send_mail
from django.conf import settings
import urllib.request, urllib.parse, json

def home(request):
    latest_news = News.objects.filter(is_published=True).order_by('-created_at')[:4]
    upcoming_events = Event.objects.filter(date__gte=timezone.now(), is_active=True).order_by('date')[:3]
    return render(request, 'website/home.html', {'latest_news': latest_news, 'upcoming_events': upcoming_events})

def news_list(request):
    qs = News.objects.filter(is_published=True).order_by('-created_at')
    query = request.GET.get('q')
    if query:
        qs = qs.filter(title__icontains=query) | qs.filter(content__icontains=query)
        qs = qs.distinct()
    paginator = Paginator(qs, 10)
    page = request.GET.get('page')
    items = paginator.get_page(page)
    return render(request, 'website/news/list.html', {'items': items})

def news_detail(request, slug):
    item = get_object_or_404(News, slug=slug, is_published=True)
    comments = Comment.objects.filter(content_type=ContentType.objects.get_for_model(News), object_id=item.pk)
    comment_form = CommentForm()
    return render(request, 'website/news/detail.html', {'item': item, 'comments': comments, 'comment_form': comment_form})

def events_list(request):
    now = timezone.now()
    # Upcoming events split by type
    upcoming = Event.objects.filter(date__gte=now, is_active=True).order_by('date')
    foreign_events = upcoming.filter(is_international=True)
    local_events = upcoming.filter(is_international=False)
    
    past = Event.objects.filter(date__lt=now).order_by('-date')
    
    context = {
        'foreign_events': foreign_events, 
        'local_events': local_events,
        'past': past
    }
    return render(request, 'website/events/list.html', context)

def event_detail(request, slug):
    event = get_object_or_404(Event, slug=slug)
    comments = Comment.objects.filter(content_type=ContentType.objects.get_for_model(Event), object_id=event.pk)
    comment_form = CommentForm()
    return render(request, 'website/events/detail.html', {'event': event, 'comments': comments, 'comment_form': comment_form})

def publications_list(request):
    qs = Publication.objects.select_related('category').all().order_by('-year', '-created_at')
    year = request.GET.get('year')
    cat = request.GET.get('category')
    if year:
        qs = qs.filter(year=year)
    if cat:
        qs = qs.filter(category__slug=cat)
    categories = PublicationCategory.objects.all()
    paginator = Paginator(qs, 10)
    page = request.GET.get('page')
    items = paginator.get_page(page)
    return render(request, 'website/publications/list.html', {'items': items, 'categories': categories})

def publication_detail(request, slug):
    pub = get_object_or_404(Publication, slug=slug)
    comments = Comment.objects.filter(content_type=ContentType.objects.get_for_model(Publication), object_id=pub.pk)
    comment_form = CommentForm()
    return render(request, 'website/publications/detail.html', {'pub': pub, 'comments': comments, 'comment_form': comment_form})

def about(request):
    return render(request, 'website/about.html')

def president_bio(request):
    return render(request, 'website/president.html')

def membership(request):
    types = MembershipType.objects.all()
    applied = request.GET.get('applied') == '1'
    return render(request, 'website/membership.html', {'types': types, 'applied': applied})

@login_required
def membership_apply(request, slug):
    mtype = get_object_or_404(MembershipType, slug=slug)
    if request.method == 'POST':
        form = MembershipApplicationForm(request.POST)
        if form.is_valid():
            app = form.save(commit=False)
            app.user = request.user
            app.membership_type = mtype
            app.save()
            # redirect to membership page with flag (payment step can be integrated later)
            return redirect(reverse('membership') + '?applied=1')
    else:
        form = MembershipApplicationForm()
    return render(request, 'website/membership_apply.html', {'form': form, 'mtype': mtype})

def contacts(request):
    sent = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        # optional subject (used by membership quick form)
        subject = request.POST.get('subject', '').strip()
        # reCAPTCHA verification (only if secret set)
        recaptcha_ok = True
        secret = getattr(settings, 'RECAPTCHA_SECRET_KEY', '')
        recaptcha_response = request.POST.get('g-recaptcha-response') or request.POST.get('recaptcha_token')
        if secret:
            recaptcha_ok = False
            if recaptcha_response:
                data = urllib.parse.urlencode({
                    'secret': secret,
                    'response': recaptcha_response,
                    'remoteip': request.META.get('REMOTE_ADDR')
                }).encode()
                try:
                    resp = urllib.request.urlopen('https://www.google.com/recaptcha/api/siteverify', data)
                    result = json.loads(resp.read().decode())
                    recaptcha_ok = result.get('success', False) and result.get('score', 0) >= 0.3
                except Exception:
                    recaptcha_ok = False

        if form.is_valid() and recaptcha_ok:
            obj = form.save()
            # send notification email to CONTACT_EMAIL (non-blocking note: console backend for dev)
            try:
                mail_subject = f'Новое сообщение с сайта: {subject or "Контакты"}'
                mail_body = f"От: {obj.name} <{obj.email}>\n\n{obj.message}"
                send_mail(mail_subject, mail_body, settings.DEFAULT_FROM_EMAIL, [getattr(settings, 'CONTACT_EMAIL')], fail_silently=True)
            except Exception:
                pass
            sent = True
            form = ContactForm()
        else:
            # if recaptcha failed, add non-field error
            if not recaptcha_ok:
                form.add_error(None, 'reCAPTCHA verification failed. Попробуйте позже.')
    else:
        form = ContactForm()
    return render(request, 'website/contacts.html', {'form': form, 'sent': sent})

@login_required
def add_comment(request):
    if request.method != 'POST':
        return redirect('home')
    model_name = request.POST.get('model')
    slug = request.POST.get('slug')
    content = request.POST.get('content')
    model_map = {'news': News, 'event': Event, 'publication': Publication}
    Model = model_map.get(model_name)
    if not Model:
        return redirect('home')
    try:
        obj = Model.objects.get(slug=slug)
    except Model.DoesNotExist:
        return redirect('home')
    ct = ContentType.objects.get_for_model(Model)
    Comment.objects.create(user=request.user, content_type=ct, object_id=obj.pk, content=content)
    # redirect back to detail
    if model_name == 'news':
        return redirect('news_detail', slug=slug)
    if model_name == 'event':
        return redirect('event_detail', slug=slug)
    return redirect('publication_detail', slug=slug)

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

# New: handle /accounts/profile/ (redirect to home)
def profile_redirect(request):
    if request.user.is_authenticated:
        return redirect('home')
    return redirect('login')

# New: logout view that accepts GET and POST and redirects to home
def logout_view(request):
    if request.method not in ('GET', 'POST'):
        return HttpResponseNotAllowed(['GET', 'POST'])
    logout(request)
    return redirect('home')

def about_history(request):
    return render(request, 'website/about_history.html')

def about_statutes(request):
    return render(request, 'website/about_statutes.html')

def membership_benefits(request):
    return render(request, 'website/membership_benefits.html')

def about_international(request):
    return render(request, 'website/about_international.html')

def congress_past(request):
    # Fetch all past events, ordered by date descending
    past_events = Event.objects.filter(date__lt=timezone.now(), is_active=False).order_by('-date')
    return render(request, 'website/congress_past.html', {'events': past_events})

def generic_page(request, title="Страница"):

    context = {
        'title': title,
        'content': 'Информация в данном разделе находится в стадии наполнения.'
    }
    return render(request, 'website/generic.html', context)
