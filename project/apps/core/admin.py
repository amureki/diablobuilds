# coding: utf-8
from django.contrib import admin

from django_markdown.admin import MarkdownModelAdmin

from project.apps.core.models import Build, Guest, Vote, News, Version


class BuildAdmin(MarkdownModelAdmin):
    list_display = (u'id', u'name', u'published')
    list_display_links = (u'id', u'name',)
    list_filter = (u'published',)


class VoteInline(admin.StackedInline):
    model = Vote
    extra = 0
    readonly_fields = (u'date_voted',)


class GuestAdmin(admin.ModelAdmin):
    list_display = (u'id', u'ip', u'path', u'date_modified',)
    list_display_links = (u'id', u'ip',)
    list_filter = (u'path',)
    inlines = (VoteInline,)


class NewsAdmin(admin.ModelAdmin):
    list_display = (u'id', u'title', u'date_created',)
    list_display_links = (u'id', u'title', u'date_created',)


admin.site.register(Build, BuildAdmin)
admin.site.register(Vote)
admin.site.register(Guest, GuestAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Version)