from django import forms
from django.core.exceptions import ValidationError
from .models import ContactMessage, Comment, MembershipApplication
import os

def validate_file_size_and_type(file):
    max_size = 5 * 1024 * 1024  # 5MB
    if file.size > max_size:
        raise ValidationError("Размер файла не должен превышать 5МБ.")
    
    ext = os.path.splitext(file.name)[1].lower()
    valid_extensions = ['.pdf', '.jpg', '.jpeg', '.png']
    if ext not in valid_extensions:
        raise ValidationError("Допустимые форматы: PDF, JPG, PNG.")
    
    # Optional: check MIME type if needed, but extension + size is a good baseline

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

    def clean_content(self):
        content = self.cleaned_data.get('content', '').strip()
        if not content:
            raise ValidationError("Комментарий не может быть пустым.")
        if len(content) > 2000:
            raise ValidationError("Комментарий слишком длинный (макс. 2000 символов).")
        return content

COUNTRIES = [
    ('', 'Выберите страну'),
    ('AF', 'Афганистан'), ('AL', 'Албания'), ('DZ', 'Алжир'), ('AS', 'Американское Самоа'), ('AD', 'Андорра'),
    ('AO', 'Ангола'), ('AI', 'Ангилья'), ('AQ', 'Антарктида'), ('AG', 'Антигуа и Барбуда'), ('AR', 'Аргентина'),
    ('AM', 'Армения'), ('AW', 'Аруба'), ('AU', 'Австралия'), ('AT', 'Австрия'), ('AZ', 'Азербайджан'),
    ('BS', 'Багамские острова'), ('BH', 'Бахрейн'), ('BD', 'Бангладеш'), ('BB', 'Барбадос'), ('BY', 'Беларусь'),
    ('BE', 'Бельгия'), ('BZ', 'Белиз'), ('BJ', 'Бенин'), ('BM', 'Бермудские острова'), ('BT', 'Бутан'),
    ('BO', 'Боливия'), ('BA', 'Босния и Герцеговина'), ('BW', 'Ботсвана'), ('BR', 'Бразилия'), ('BN', 'Бруней'),
    ('BG', 'Болгария'), ('BF', 'Буркина-Фасо'), ('BI', 'Бурунди'), ('KH', 'Камбоджа'), ('CM', 'Камерун'),
    ('CA', 'Канада'), ('CV', 'Кабо-Верде'), ('KY', 'Каймановы острова'), ('CF', 'Центральноафриканская Республика'), ('TD', 'Чад'),
    ('CL', 'Чили'), ('CN', 'Китай'), ('CX', 'Остров Рождества'), ('CC', 'Кокосовые острова'), ('CO', 'Колумбия'),
    ('KM', 'Коморские острова'), ('CG', 'Конго'), ('CD', 'Конго, демократическая республика'), ('CK', 'Острова Кука'), ('CR', 'Коста-Рика'),
    ('CI', 'Кот-д\'Ивуар'), ('HR', 'Хорватия'), ('CU', 'Куба'), ('CY', 'Кипр'), ('CZ', 'Чехия'),
    ('DK', 'Дания'), ('DJ', 'Джибути'), ('DM', 'Доминика'), ('DO', 'Доминиканская Республика'), ('EC', 'Эквадор'),
    ('EG', 'Египет'), ('SV', 'Сальвадор'), ('GQ', 'Экваториальная Гвинея'), ('ER', 'Эритрея'), ('EE', 'Эстония'),
    ('ET', 'Эфиопия'), ('FK', 'Фолклендские острова'), ('FO', 'Фарерские острова'), ('FJ', 'Фиджи'), ('FI', 'Финляндия'),
    ('FR', 'Франция'), ('GF', 'Французская Гвиана'), ('PF', 'Французская Полинезия'), ('GA', 'Габон'), ('GM', 'Гамбия'),
    ('GE', 'Грузия'), ('DE', 'Германия'), ('GH', 'Гана'), ('GI', 'Гибралтар'), ('GR', 'Греция'),
    ('GL', 'Гренландия'), ('GD', 'Гренада'), ('GP', 'Гваделупа'), ('GU', 'Гуам'), ('GT', 'Гватемала'),
    ('GN', 'Гвинея'), ('GW', 'Гвинея-Бисау'), ('GY', 'Гайана'), ('HT', 'Гаити'), ('HN', 'Гондурас'),
    ('HK', 'Гонконг'), ('HU', 'Венгрия'), ('IS', 'Исландия'), ('IN', 'Индия'), ('ID', 'Индонезия'),
    ('IR', 'Иран'), ('IQ', 'Ирак'), ('IE', 'Ирландия'), ('IL', 'Израиль'), ('IT', 'Италия'),
    ('JM', 'Ямайка'), ('JP', 'Япония'), ('JO', 'Иордания'), ('KZ', 'Казахстан'), ('KE', 'Кения'),
    ('KI', 'Кирибати'), ('KP', 'Корея, Северная'), ('KR', 'Корея, Южная'), ('KW', 'Кувейт'), ('KG', 'Кыргызстан'),
    ('LA', 'Лаос'), ('LV', 'Латвия'), ('LB', 'Ливан'), ('LS', 'Лесото'), ('LR', 'Либерия'),
    ('LY', 'Ливия'), ('LI', 'Лихтенштейн'), ('LT', 'Литва'), ('LU', 'Люксембург'), ('MO', 'Макао'),
    ('MK', 'Македония'), ('MG', 'Мадагаскар'), ('MW', 'Малави'), ('MY', 'Малайзия'), ('MV', 'Мальдивы'),
    ('ML', 'Мали'), ('MT', 'Мальта'), ('MH', 'Маршалловы острова'), ('MQ', 'Мартиника'), ('MR', 'Мавритания'),
    ('MU', 'Маврикий'), ('YT', 'Майотта'), ('MX', 'Мексика'), ('FM', 'Микронезия'), ('MD', 'Молдова'),
    ('MC', 'Монако'), ('MN', 'Монголия'), ('MS', 'Монтсеррат'), ('MA', 'Марокко'), ('MZ', 'Мозамбик'),
    ('MM', 'Мьянма'), ('NA', 'Намибия'), ('NR', 'Науру'), ('NP', 'Непал'), ('NL', 'Нидерланды'),
    ('AN', 'Нидерландские Антильские острова'), ('NC', 'Новая Каледония'), ('NZ', 'Новая Зеландия'), ('NI', 'Никарагуа'), ('NE', 'Нигер'),
    ('NG', 'Нигерия'), ('NU', 'Ниуэ'), ('NF', 'Норфолк'), ('MP', 'Северные Марианские острова'), ('NO', 'Норвегия'),
    ('OM', 'Оман'), ('PK', 'Пакистан'), ('PW', 'Палау'), ('PS', 'Палестина'), ('PA', 'Панама'),
    ('PG', 'Папуа - Новая Гвинея'), ('PY', 'Парагвай'), ('PE', 'Перу'), ('PH', 'Филиппины'), ('PN', 'Питкэрн'),
    ('PL', 'Польша'), ('PT', 'Португалия'), ('PR', 'Пуэрто-Рико'), ('QA', 'Катар'), ('RE', 'Реюньон'),
    ('RO', 'Румыния'), ('RU', 'Россия'), ('RW', 'Руанда'), ('SH', 'Святая Елена'), ('KN', 'Сент-Китс и Невис'),
    ('LC', 'Сент-Люсия'), ('PM', 'Сент-Пьер и Микелон'), ('VC', 'Сент-Винсент и Гренадины'), ('WS', 'Самоа'), ('SM', 'Сан-Марино'),
    ('ST', 'Сан-Томе и Принсипи'), ('SA', 'Саудовская Аравия'), ('SN', 'Сенегал'), ('CS', 'Сербия и Черногория'), ('SC', 'Сейшельские острова'),
    ('SL', 'Сьерра-Леоне'), ('SG', 'Сингапур'), ('SK', 'Словакия'), ('SI', 'Словения'), ('SB', 'Соломоновы острова'),
    ('SO', 'Сомали'), ('ZA', 'Южная Африка'), ('ES', 'Испания'), ('LK', 'Шри-Ланка'), ('SD', 'Судан'),
    ('SR', 'Суринам'), ('SJ', 'Шпицберген и Ян-Майен'), ('SZ', 'Свазиленд'), ('SE', 'Швеция'), ('CH', 'Швейцария'),
    ('SY', 'Сирия'), ('TW', 'Тайвань'), ('TJ', 'Таджикистан'), ('TZ', 'Танзания'), ('TH', 'Таиланд'),
    ('TG', 'Того'), ('TK', 'Токелау'), ('TO', 'Тонга'), ('TT', 'Тринидад и Тобаго'), ('TN', 'Тунис'),
    ('TR', 'Турция'), ('TM', 'Туркменистан'), ('TC', 'Тёркс и Кайкос'), ('TV', 'Тувалу'), ('UG', 'Уганда'),
    ('UA', 'Украина'), ('AE', 'Объединенные Арабские Эмираты'), ('GB', 'Великобритания'), ('US', 'США'), ('UY', 'Уругвай'),
    ('UZ', 'Узбекистан'), ('VU', 'Вануату'), ('VA', 'Ватикан'), ('VE', 'Венесуэла'), ('VN', 'Вьетнам'),
    ('VG', 'Виргинские острова (Британия)'), ('VI', 'Виргинские острова (США)'), ('WF', 'Уоллис и Футуна'), ('EH', 'Западная Сахара'), ('YE', 'Йемен'),
    ('ZM', 'Замбия'), ('ZW', 'Зимбабве')
]

class MembershipApplicationForm(forms.ModelForm):
    country = forms.ChoiceField(choices=COUNTRIES, widget=forms.Select(attrs={'class': 'form-select'}), label="Страна", required=True)

    class Meta:
        model = MembershipApplication
        fields = [
            'full_name', 'birth_date', 'place_of_work', 'job_title',
            'specialty', 'qualification', 'degree', 'experience',
            'country', 'city', 'phone', 'email',
            'id_card_copy', 'payment_receipt', 'agreement_accepted'
        ]
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Иванов Иван Иванович'}),
            'birth_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'place_of_work': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'название медицинской организации'}),
            'job_title': forms.TextInput(attrs={'class': 'form-control'}),
            'specialty': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'травматология и ортопедия'}),
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

    def clean_id_card_copy(self):
        file = self.cleaned_data.get('id_card_copy')
        if file:
            validate_file_size_and_type(file)
        return file

    def clean_payment_receipt(self):
        file = self.cleaned_data.get('payment_receipt')
        if file:
            validate_file_size_and_type(file)
        return file

from django.contrib.auth.models import User

class MembershipRegistrationForm(forms.ModelForm):
    # User fields
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username (для входа)'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    country = forms.ChoiceField(choices=COUNTRIES, widget=forms.Select(attrs={'class': 'form-select'}), label="Страна", required=True)

    class Meta:
        model = MembershipApplication
        fields = [
            'full_name', 'birth_date', 'place_of_work', 'job_title',
            'specialty', 'qualification', 'degree', 'experience',
            'country', 'city', 'phone',
            'id_card_copy', 'agreement_accepted'
        ]
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Иванов Иван Иванович'}),
            'birth_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'place_of_work': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'название медицинской организации'}),
            'job_title': forms.TextInput(attrs={'class': 'form-control'}),
            'specialty': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'травматология и ортопедия'}),
            'qualification': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'врач-травматолог первой категории'}),
            'degree': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'PhD, кандидат медицинских наук и т.д.'}),
            'experience': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '15 лет'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Алматы'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+7 777 ...'}),
            'id_card_copy': forms.FileInput(attrs={'class': 'form-control', 'accept': '.pdf,.jpg,.png'}),
            'agreement_accepted': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }

    def clean_id_card_copy(self):
        file = self.cleaned_data.get('id_card_copy')
        if file:
            validate_file_size_and_type(file)
        return file

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
