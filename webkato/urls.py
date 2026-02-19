from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('news/', views.news_list, name='news_list'),
    path('news/<slug:slug>/', views.news_detail, name='news_detail'),
    # news-specific comment URL removed — используется общий путь ниже

    path('events/', views.events_list, name='events_list'),
    path('events/<slug:slug>/', views.event_detail, name='event_detail'),
    # event-specific comment URL removed

    path('publications/', views.publications_list, name='publications_list'),
    path('publications/<slug:slug>/', views.publication_detail, name='publication_detail'),
    # publication-specific comment URL removed

    # universal endpoint for posting comments (templates post here)
    path('comment/add/', views.add_comment, name='add_comment'),

    # handle default Django profile redirect after login
    path('accounts/profile/', views.profile_redirect, name='profile'),

    path('about/', views.about, name='about'),
    path('about/president/', views.president_bio, name='president_bio'),
    path('membership/', views.membership, name='membership'),
    path('membership/apply/<slug:slug>/', views.membership_apply, name='membership_apply'),
    path('contacts/', views.contacts, name='contacts'),

    # auth
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('accounts/register/', views.register, name='register'),

    # Placeholders for new structure
    path('about/mission/', views.about, name='about_mission'), # Reuse existing about
    path('about/statutes/', views.about_statutes, name='about_statutes'),
    path('about/history/', views.about_history, name='about_history'),
    path('about/international/', views.about_international, name='about_international'),
    path('about/structure/', views.generic_page, {'title': 'Структура'}, name='about_structure'),
    path('about/honorary/', views.generic_page, {'title': 'Почетные члены'}, name='about_honorary'),

    path('membership/benefits/', views.membership_benefits, name='membership_benefits'),

    path('congress/current/', views.generic_page, {'title': 'Предстоящий съезд'}, name='congress_current'),
    path('congress/past/', views.congress_past, name='congress_past'),
    path('congress/awards/', views.generic_page, {'title': 'Награды'}, name='congress_awards'),

    path('education/webinars/', views.generic_page, {'title': 'Вебинары'}, name='education_webinars'),
    path('education/protocols/', views.generic_page, {'title': 'Клинические протоколы'}, name='education_protocols'),
    path('education/courses/', views.generic_page, {'title': 'Образовательные курсы'}, name='education_courses'),

    path('fellowships/', views.generic_page, {'title': 'Гранты и стажировки'}, name='fellowships'),
    path('fellowships/visiting/', views.generic_page, {'title': 'Визитинг-профессора'}, name='fellowships_visiting'),

    path('cooperation/', views.generic_page, {'title': 'Сотрудничество'}, name='cooperation'),
]
