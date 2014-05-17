# coding: utf-8
from urlparse import urlparse
from django import forms

from project.apps.core.models import Build


class CreateForm(forms.ModelForm):
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
        if url.netloc and not url.netloc == valid_domain:
            raise forms.ValidationError(u'Введите ссылку на ролик на Youtube')
        return self.cleaned_data[u'youtube']

    email = forms.EmailField(
        widget=forms.TextInput(attrs={u'class': u'form-control', u'type': 'email'}),
        error_messages={'invalid': u'Пожалуйста, введите корректный e-mail адрес.'}
    )

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