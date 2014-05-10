# coding: utf-8
from django.forms import ModelForm, HiddenInput, Form, CharField
from project.apps.core.models import Build


class CreateForm(ModelForm):

    # def __init__(self, *args, **kwargs):
    #     super(ProductOfferInlineFormAdmin, self).__init__(*args, **kwargs)
    #     instance = kwargs.get(u'instance')
    #     if instance:
    #         self.fields[u'size'].initial = instance.product_offer.size.size

    class Meta:
        model = Build
        exclude = (u'published', u'diablo_version', u'rating',)