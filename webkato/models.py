from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class NewsCategory(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(max_length=140, unique=True)

    class Meta:
        verbose_name = 'Категория новости'
        verbose_name_plural = 'Категории новостей'

    def __str__(self):
        return self.name

class News(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    category = models.ForeignKey(NewsCategory, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.FileField(upload_to='news/', null=True, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title

class Event(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    date = models.DateTimeField()
    # Optional manual date text (e.g. "13-14 октября 2016 г.")
    date_text = models.CharField(max_length=100, blank=True, verbose_name="Текст даты (вручную)")
    location = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    image = models.FileField(upload_to='events/', null=True, blank=True)
    # Optional external URL for the event (e.g. registration page, conference site)
    external_link = models.URLField(max_length=500, blank=True, null=True, help_text='Optional external URL for the conference (registration page, etc.)')
    program_pdf = models.FileField(upload_to='events/programs/', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_international = models.BooleanField(default=False, verbose_name="Зарубежное мероприятие")

    class Meta:
        ordering = ['-date']
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'

    def __str__(self):
        return self.title

class PublicationCategory(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(max_length=140, unique=True)

    class Meta:
        verbose_name = 'Категория публикации'
        verbose_name_plural = 'Категории публикаций'

    def __str__(self):
        return self.name

class Publication(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    category = models.ForeignKey(PublicationCategory, on_delete=models.SET_NULL, null=True, blank=True)
    year = models.PositiveSmallIntegerField(null=True, blank=True)
    authors = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    pdf = models.FileField(upload_to='publications/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-year', '-created_at']
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'

    def __str__(self):
        return self.title

class ContactMessage(models.Model):
    name = models.CharField(max_length=140)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Сообщение контакта'
        verbose_name_plural = 'Сообщения контактов'

    def __str__(self):
        return f'{self.name} — {self.email}'

# New models: комментарии и мембершип
class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f'Комментарий {self.user} к {self.content_object}'

class MembershipType(models.Model):
    name = models.CharField(max_length=140)
    slug = models.SlugField(max_length=160, unique=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Тип членства'
        verbose_name_plural = 'Типы членства'

    def __str__(self):
        return self.name

class MembershipApplication(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    membership_type = models.ForeignKey(MembershipType, on_delete=models.SET_NULL, null=True)
    
    # New detailed fields
    full_name = models.CharField(max_length=255, verbose_name="ФИО", default="")
    birth_date = models.DateField(null=True, blank=True, verbose_name="Дата рождения")
    citizenship = models.CharField(max_length=100, verbose_name="Гражданство", default="")
    degree = models.CharField(max_length=100, blank=True, verbose_name="Ученая степень")
    job_title = models.CharField(max_length=150, verbose_name="Должность", default="")
    place_of_work = models.CharField(max_length=255, verbose_name="Место работы", default="")
    phone = models.CharField(max_length=20, verbose_name="Телефон", default="")

    additional_info = models.TextField(blank=True, verbose_name="Дополнительная информация")
    is_paid = models.BooleanField(default=False, verbose_name="Оплачено")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Заявка на членство'
        verbose_name_plural = 'Заявки на членство'

    def __str__(self):
        return f'{self.full_name or self.user} — {self.membership_type}'
