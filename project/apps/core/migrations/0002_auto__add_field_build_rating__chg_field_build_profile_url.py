# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Build.rating'
        db.add_column(u'core_build', 'rating',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


        # Changing field 'Build.profile_url'
        db.alter_column(u'core_build', 'profile_url', self.gf('django.db.models.fields.URLField')(max_length=255, null=True))

    def backwards(self, orm):
        # Deleting field 'Build.rating'
        db.delete_column(u'core_build', 'rating')


        # Changing field 'Build.profile_url'
        db.alter_column(u'core_build', 'profile_url', self.gf('django.db.models.fields.URLField')(default=0, max_length=255))

    models = {
        u'core.build': {
            'Meta': {'object_name': 'Build'},
            'author': ('django.db.models.fields.CharField', [], {'default': "u'Guest'", 'max_length': '255'}),
            'calculator_url': ('django.db.models.fields.URLField', [], {'max_length': '255'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'diablo_version': ('django.db.models.fields.CharField', [], {'default': "u'2.0.4'", 'max_length': '255'}),
            'hero_class': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'profile_url': ('django.db.models.fields.URLField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'rating': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'youtube': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['core']