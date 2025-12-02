from django.contrib import admin
from django.utils.html import format_html
from django.contrib import messages
from .models import (
    NewsCategory, News,
    Event,
    PublicationCategory, Publication,
    ContactMessage,
    Comment, MembershipType, MembershipApplication
)

@admin.register(NewsCategory)
class NewsCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'is_published', 'admin_image')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('category', 'is_published', 'created_at')
    search_fields = ('title', 'content', 'category__name')
    actions = ['make_published', 'make_unpublished']

    def admin_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height:60px;"/>', obj.image.url)
        return '-'
    admin_image.short_description = 'Изображение'

    def make_published(self, request, queryset):
        updated = queryset.update(is_published=True)
        self.message_user(request, f'Опубликовано {updated} запись(ей).', level=messages.SUCCESS)
    make_published.short_description = 'Опубликовать выбранные новости'

    def make_unpublished(self, request, queryset):
        updated = queryset.update(is_published=False)
        self.message_user(request, f'Снято с публикации {updated} запись(ей).', level=messages.INFO)
    make_unpublished.short_description = 'Снять публикацию у выбранных новостей'

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location', 'is_active', 'admin_image')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('is_active', 'date')
    search_fields = ('title', 'description', 'location')

    def admin_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height:60px;"/>', obj.image.url)
        return '-'
    admin_image.short_description = 'Изображение'

@admin.register(PublicationCategory)
class PublicationCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)

@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'year', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('category', 'year')
    search_fields = ('title', 'authors', 'description')

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    readonly_fields = ('name', 'email', 'message', 'created_at')
    search_fields = ('name', 'email', 'message')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'content_object', 'created_at')
    search_fields = ('user__username', 'content')

@admin.register(MembershipType)
class MembershipTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(MembershipApplication)
class MembershipApplicationAdmin(admin.ModelAdmin):
    list_display = ('user', 'membership_type', 'is_paid', 'created_at')
    list_filter = ('is_paid', 'membership_type')
    readonly_fields = ('created_at',)
