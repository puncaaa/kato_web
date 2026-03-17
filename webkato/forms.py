from django import forms
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
        fields = [
            'full_name', 'birth_date', 'place_of_work', 'job_title',
            'qualification', 'degree', 'experience',
            'city', 'phone', 'email',
            'id_card_copy', 'payment_receipt', 'agreement_accepted'
        ]
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Иванов Иван Иванович'}),
            'birth_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'place_of_work': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'название медицинской организации'}),
            'job_title': forms.TextInput(attrs={'class': 'form-control'}),
            'qualification': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'врач-травматолог первой категории'}),
            'degree': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'PhD, кандидат медицинских наук и т.д.'}),
            'experience': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '15 лет'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'id_card_copy': forms.FileInput(attrs={'class': 'form-control', 'accept': '.pdf,.jpg,.png'}),
            'payment_receipt': forms.FileInput(attrs={'class': 'form-control', 'accept': '.pdf,.jpg,.png'}),
            'agreement_accepted': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }
from django.contrib.auth.models import User

class MembershipRegistrationForm(forms.ModelForm):
    # User fields
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username (для входа)'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))

    class Meta:
        model = MembershipApplication
        fields = [
            'full_name', 'birth_date', 'place_of_work', 'job_title',
            'qualification', 'degree', 'experience',
            'city', 'phone',
            'id_card_copy', 'agreement_accepted'
        ]
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Иванов Иван Иванович'}),
            'birth_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'place_of_work': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'название медицинской организации'}),
            'job_title': forms.TextInput(attrs={'class': 'form-control'}),
            'qualification': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'врач-травматолог первой категории'}),
            'degree': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'PhD, кандидат медицинских наук и т.д.'}),
            'experience': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '15 лет'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Алматы'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+7 777 ...'}),
            'id_card_copy': forms.FileInput(attrs={'class': 'form-control', 'accept': '.pdf,.jpg,.png'}),
            'agreement_accepted': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Пользователь с таким именем уже существует.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Пользователь с таким email уже существует.")
        return email
