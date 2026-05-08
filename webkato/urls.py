from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('news/', views.news_list, name='news_list'),
    path('news/<slug:slug>/', views.news_detail, name='news_detail'),


    path('events/', views.events_list, name='events_list'),
    path('events/<slug:slug>/', views.event_detail, name='event_detail'),


    path('publications/', views.publications_list, name='publications_list'),
    path('publications/<slug:slug>/', views.publication_detail, name='publication_detail'),


    path('comment/add/', views.add_comment, name='add_comment'),

    path('accounts/profile/', views.profile_redirect, name='profile'),

    path('about/', views.about, name='about'),
    path('about/president/', views.president_bio, name='president_bio'),
    path('membership/', views.membership, name='membership'),
    path('membership/apply/<slug:slug>/', views.membership_apply, name='membership_apply'),
    path('membership/register/<slug:slug>/', views.membership_register, name='membership_register'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('payment/success/', views.payment_success, name='payment_success'),
    path('payment/fail/', views.payment_fail, name='payment_fail'),
    path('contacts/', views.contacts, name='contacts'),

    # auth
    path('accounts/login/', views.RateLimitedLoginView.as_view(), name='login'),
    path('accounts/logout/', views.logout_view, name='logout'),

    # password reset
    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'), name='password_reset'),
    path('accounts/password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),


    path('about/mission/', views.about, name='about_mission'), 
    path('about/statutes/', views.about_statutes, name='about_statutes'),
    path('about/ethics/', views.about_ethics, name='about_ethics'),
    path('about/history/', views.about_history, name='about_history'),
    path('about/international/', views.about_international, name='about_international'),
    path('about/structure/', views.generic_page, {'title': 'Структура'}, name='about_structure'),
    path('about/founder/', views.about_founder, name='about_founder'),

    path('membership/benefits/', views.membership_benefits, name='membership_benefits'),

    path('congress/current/', views.congress_current, name='congress_current'),
    path('congress/past/', views.congress_past, name='congress_past'),
    path('congress/awards/', views.generic_page, {'title': 'Награды'}, name='congress_awards'),

    path('education/webinars/', views.generic_page, {'title': 'Вебинары'}, name='education_webinars'),
    path('education/protocols/', views.generic_page, {'title': 'Клинические протоколы'}, name='education_protocols'),
    path('education/courses/', views.education_courses, name='education_courses'),

    path('fellowships/', views.generic_page, {'title': 'Гранты и стажировки'}, name='fellowships'),
    path('fellowships/visiting/', views.generic_page, {'title': 'Визитинг-профессора'}, name='fellowships_visiting'),

    path('cooperation/', views.generic_page, {'title': 'Сотрудничество'}, name='cooperation'),
]
