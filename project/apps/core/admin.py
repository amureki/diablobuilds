# coding: utf-8
from django.contrib import admin

from django_markdown.admin import MarkdownModelAdmin

from project.apps.core.models import Build, Guest, Vote


class VoteInline(admin.StackedInline):
    model = Vote
    extra = 0


class GuestAdmin(admin.ModelAdmin):
    list_display = (u'id', u'ip', u'path', u'date_modified',)
    list_display_links = (u'id', u'ip',)
    list_filter = (u'path',)
    inlines = (VoteInline,)


# admin.site.register(Build)
admin.site.register(Build, MarkdownModelAdmin)
admin.site.register(Guest, GuestAdmin)