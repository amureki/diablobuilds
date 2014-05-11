# coding: utf-8
import re
from django.core.urlresolvers import reverse
from django.db import models


class Build(models.Model):
    BARBARIAN = 0
    WITCH_DOCTOR = 1
    CRUSADER = 2
    MONK = 3
    DEMON_HUNTER = 4
    WIZARD = 5

    HERO_CLASSES = (
        (BARBARIAN, u'Варвар'),
        (WITCH_DOCTOR, u'Колдун'),
        (CRUSADER, u'Крестоносец'),
        (MONK, u'Монах'),
        (DEMON_HUNTER, u'Охотник на демонов'),
        (WIZARD, u'Чародей'),
    )

    author = models.CharField(u'Автор', max_length=255, default=u'Гость')
    name = models.CharField(u'Название', max_length=255)
    hero_class = models.IntegerField(u'Класс', choices=HERO_CLASSES, default=0)
    calculator_url = models.URLField(u'Ссылка на калькулятор', max_length=255)
    profile_url = models.URLField(u'Ссылка на профиль', max_length=255, blank=True, null=True)
    diablo_version = models.CharField(u'Версия игры', max_length=255, default=u'2.0.4')
    description = models.TextField(u'Описание')
    youtube = models.URLField(u'Ссылка на youtube', max_length=255, blank=True, null=True)
    rating = models.IntegerField(u'Рейтинг', default=0)

    published = models.BooleanField(u'Опубликован', default=False)

    date_created = models.DateTimeField(u'Дата создания', auto_now_add=True)

    class Meta:
        verbose_name = u'Билд'
        verbose_name_plural = u'Билды'
        ordering = (u'-rating', u'-id')

    def get_absolute_url(self):
        return reverse(u'build_detail', args=(self.id,))

    def get_youtube_embed(self):
        match = re.search(r'^(http|https)\:\/\/www\.youtube\.com\/watch\?v\=(\w*)(\&(.*))?$', self.youtube)
        if match:
            url = u'http://www.youtube.com/embed/%s' % (match.group(2))
            embed = u'<iframe width="560" height="315" src="%s" frameborder="0" allowfullscreen></iframe>' % url
            return embed
        return None

    def rate_up(self):
        self.rating += 1
        self.save()

    def rate_down(self):
        self.rating -= 1
        self.save()

    def __unicode__(self):
        return self.name


class Guest(models.Model):
    ip = models.CharField(u'ip-адрес', max_length=255, default=0)
    rated_builds = models.ManyToManyField(Build, verbose_name=u'Оцененные билды', blank=True, null=True)

    path = models.CharField(u'Последний запрос', max_length=255, null=True, blank=True)
    referrer = models.TextField(u'Последний Referrer', null=True, blank=True)
    user_agent = models.TextField(u'Последний User Agent', null=True, blank=True)

    date_created = models.DateTimeField(u'Дата создания', auto_now_add=True)
    date_modified = models.DateTimeField(u'Дата изменения', auto_now=True)

    class Meta:
        verbose_name = u'Гость'
        verbose_name_plural = u'Гости'
        ordering = (u'ip',)

    def __unicode__(self):
        return self.ip