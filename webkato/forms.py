from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import ContactMessage, Comment, MembershipApplication

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows':3, 'class':'form-control', 'placeholder':'Оставьте комментарий'}),
        }

class MembershipApplicationForm(forms.ModelForm):
    class Meta:
        model = MembershipApplication
        fields = ['full_name', 'birth_date', 'citizenship', 'degree', 'job_title', 'place_of_work', 'phone', 'additional_info']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Иванов Иван Иванович'}),
            'birth_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'citizenship': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Республика Казахстан'}),
            'degree': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Доктор медицинских наук'}),
            'job_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Заведующий отделением'}),
            'place_of_work': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Городская больница №1'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+7 700 000 00 00'}),
            'additional_info': forms.Textarea(attrs={'rows':3, 'class':'form-control', 'placeholder':'Другая важная информация'}),
        }

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class':'form-control'}))
    class Meta:
        model = get_user_model()
        fields = ("username", "email", "password1", "password2")
