# coding: utf-8
from urlparse import urlparse
from django import forms

from project.apps.core.models import Build


class CreateForm(forms.ModelForm):

    # def __init__(self, *args, **kwargs):
    #     super(ProductOfferInlineFormAdmin, self).__init__(*args, **kwargs)
    #     instance = kwargs.get(u'instance')
    #     if instance:
    #         self.fields[u'size'].initial = instance.product_offer.size.size

    # def clean_email(self):
    #     if User.objects.filter(email__iexact=self.cleaned_data[u'email']).exists():
    #         raise forms.ValidationError(u'Данный почтовый ящик уже используется')
    #     return self.cleaned_data[u'email']
    #
    # def clean_password(self):
    #     password = self.cleaned_data.get(u'password', u'')
    #     if not len(password) >= 6:
    #         raise forms.ValidationError(u'Пароль должен быть не менее 6 символов')
    #     if password.isspace() or len(password.strip()) != len(password):
    #         raise forms.ValidationError(u'Пароль не может состоять из пробелов')
    #     return password
    #
    # def clean_phone(self):
    #     if Account.objects.filter(phone__iexact=self.cleaned_data[u'phone']).exists():
    #         raise forms.ValidationError(u'Данный телефон уже используется')
    #     return self.cleaned_data[u'phone']

    def clean_calculator_url(self):
        url = urlparse(self.cleaned_data[u'calculator_url'])
        valid_domain = u'eu.battle.net'
        if not url.netloc == valid_domain:
            raise forms.ValidationError(u'Введите ссылку на калькулятор от Blizzard')
        return self.cleaned_data[u'calculator_url']

    def clean_profile_url(self):
        url = urlparse(self.cleaned_data[u'profile_url'])
        valid_domain = u'eu.battle.net'
        if not url.netloc == valid_domain:
            raise forms.ValidationError(u'Введите ссылку на профиль на сайте Blizzard')
        return self.cleaned_data[u'profile_url']

    def clean_youtube(self):
        url = urlparse(self.cleaned_data[u'youtube'])
        valid_domain = u'youtube.com'
        if not url.netloc == valid_domain:
            raise forms.ValidationError(u'Введите ссылку на ролик на Youtube')
        return self.cleaned_data[u'youtube']

    class Meta:
        model = Build
        exclude = (u'published', u'diablo_version', u'rating',)
        widgets = {
            u'author': forms.TextInput(attrs={u'class': u'form-control'}),
            u'name': forms.TextInput(attrs={u'class': u'form-control'}),
            u'hero_class': forms.Select(attrs={u'class': u'form-control'}),
            u'calculator_url': forms.TextInput(attrs={u'class': u'form-control'}),
            u'profile_url': forms.TextInput(attrs={u'class': u'form-control'}),
            u'description': forms.Textarea(attrs={u'data-provide':u'markdown', u'cols': 50, u'class': u'form-control'}),
            u'youtube': forms.TextInput(attrs={u'class': u'form-control'}),
        }