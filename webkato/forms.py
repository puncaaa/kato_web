from django import forms
from .models import ContactMessage, Comment

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
            'residence', 'phone', 'email',
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
            'residence': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'id_card_copy': forms.FileInput(attrs={'class': 'form-control', 'accept': '.pdf,.jpg,.png'}),
            'payment_receipt': forms.FileInput(attrs={'class': 'form-control', 'accept': '.pdf,.jpg,.png'}),
            'agreement_accepted': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }


