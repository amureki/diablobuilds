# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Build.youtube'
        db.alter_column(u'core_build', 'youtube', self.gf('django.db.models.fields.URLField')(max_length=255, null=True))

    def backwards(self, orm):

        # Changing field 'Build.youtube'
        db.alter_column(u'core_build', 'youtube', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

    models = {
        u'core.build': {
            'Meta': {'ordering': "(u'-rating', u'-id')", 'object_name': 'Build'},
            'author': ('django.db.models.fields.CharField', [], {'default': "u'\\u0413\\u043e\\u0441\\u0442\\u044c'", 'max_length': '255'}),
            'calculator_url': ('django.db.models.fields.URLField', [], {'max_length': '255'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'diablo_version': ('django.db.models.fields.CharField', [], {'default': "u'2.0.4'", 'max_length': '255'}),
            'hero_class': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'profile_url': ('django.db.models.fields.URLField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'rating': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'youtube': ('django.db.models.fields.URLField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'core.guest': {
            'Meta': {'ordering': "(u'ip',)", 'object_name': 'Guest'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.CharField', [], {'default': '0', 'max_length': '255'}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'rated_builds': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['core.Build']", 'null': 'True', 'blank': 'True'}),
            'referrer': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'user_agent': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['core']