# coding: utf-8
from django.contrib import admin

from django_markdown.admin import MarkdownModelAdmin

from project.apps.core.models import Build, Guest


class GuestAdmin(admin.ModelAdmin):
    raw_id_fields = (u'rated_builds',)
    list_display = (u'id', u'ip', u'path', u'date_modified',)
    list_display_links = (u'id', u'ip',)
    list_filter = (u'path',)


# admin.site.register(Build)
admin.site.register(Build, MarkdownModelAdmin)
admin.site.register(Guest, GuestAdmin)