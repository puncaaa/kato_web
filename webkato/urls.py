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
    path('membership/', views.membership, name='membership'),
    path('membership/apply/<slug:slug>/', views.membership_apply, name='membership_apply'),
    path('contacts/', views.contacts, name='contacts'),

    # auth
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('accounts/register/', views.register, name='register'),
]
