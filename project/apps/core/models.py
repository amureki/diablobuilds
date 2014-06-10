# coding: utf-8
import re
from datetime import datetime
from django.core.urlresolvers import reverse
from django.db import models


class PublishedBuildManager(models.Manager):
    def get_queryset(self):
        return super(PublishedBuildManager, self).get_queryset().filter(published=True)


class Build(models.Model):
    BARBARIAN = 0
    CRUSADER = 1
    DEMON_HUNTER = 2
    MONK = 3
    WITCH_DOCTOR = 4
    WIZARD = 5

    HERO_CLASSES = (
        (BARBARIAN, u'Варвар'),
        (CRUSADER, u'Крестоносец'),
        (DEMON_HUNTER, u'Охотник на демонов'),
        (MONK, u'Монах'),
        (WITCH_DOCTOR, u'Колдун'),
        (WIZARD, u'Чародей'),
    )

    author = models.CharField(u'Автор', help_text=u'Можно указать свой BattleTag', max_length=255, default=u'Гость')
    email = models.EmailField('Электронная почта', max_length=255, help_text=u'Не будет отображаться на сайте')
    name = models.CharField(u'Название билда', max_length=255)
    hero_class = models.IntegerField(u'Класс', choices=HERO_CLASSES, default=BARBARIAN)
    calculator_url = models.URLField(u'Ссылка на калькулятор Blizzard', max_length=255)
    profile_url = models.URLField(u'Ссылка на профиль Blizzard', max_length=255, blank=True, null=True)
    diablo_version = models.CharField(u'Версия игры', max_length=255, default=u'2.0.4')
    description = models.TextField(u'Описание',
                                   help_text=u'Доступна markdown-разметка ('
                                   u'<a href="http://daringfireball.net/projects/markdown/syntax" '
                                   u'rel="nofollow" target="_blank">описание</a>)'
                                   )
    youtube = models.URLField(u'Видео работы билда на youtube', max_length=255, blank=True, null=True,
                              help_text=u'Пример ссылки: http://www.youtube.com/watch?v=juT-1ew-ffc')
    rating = models.IntegerField(u'Рейтинг', default=0)

    published = models.BooleanField(u'Опубликован', default=False)

    date_created = models.DateTimeField(u'Дата создания', auto_now_add=True)

    objects = models.Manager()
    published_objects = PublishedBuildManager()

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
    rated_builds = models.ManyToManyField(Build, through=u'Vote', verbose_name=u'Оцененные билды', blank=True, null=True)

    path = models.CharField(u'Последний запрос', max_length=255, null=True, blank=True)
    referer = models.TextField(u'Последний Referer', null=True, blank=True)
    user_agent = models.TextField(u'Последний User Agent', null=True, blank=True)

    date_created = models.DateTimeField(u'Дата создания', auto_now_add=True)
    date_modified = models.DateTimeField(u'Дата изменения', auto_now=True)

    class Meta:
        verbose_name = u'Гость'
        verbose_name_plural = u'Гости'
        ordering = (u'ip',)

    def __unicode__(self):
        return self.ip


class Vote(models.Model):
    DOWN = 0
    UP = 1

    VOTE_CHOICES = (
        (DOWN, u'Вниз'),
        (UP, u'Вверх'),
    )
    build = models.ForeignKey(Build, verbose_name=u'Билд')
    guest = models.ForeignKey(Guest, verbose_name=u'Гость')
    action = models.IntegerField(u'Голос', choices=VOTE_CHOICES, default=0)
    date_voted = models.DateField(u'Дата последнего голоса', auto_now=True)

    class Meta:
        verbose_name = u'Голос'
        verbose_name_plural = u'Голоса'

    def __unicode__(self):
        return u'%s за %s' % (self.guest, self.build)


class News(models.Model):
    title = models.CharField(u'Заголовок', max_length=255, blank=True, null=True)
    text = models.TextField(u'Текст', blank=True, null=True)
    date_created = models.DateTimeField(u'Дата создания', default=datetime.now())

    class Meta:
        ordering = (u'-id',)
        verbose_name = u'Новость'
        verbose_name_plural = u'Новости'

    def __unicode__(self):
        return self.title