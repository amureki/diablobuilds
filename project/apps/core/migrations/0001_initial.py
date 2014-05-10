# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Build'
        db.create_table(u'core_build', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('author', self.gf('django.db.models.fields.CharField')(default=u'Guest', max_length=255)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('hero_class', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('calculator_url', self.gf('django.db.models.fields.URLField')(max_length=255)),
            ('profile_url', self.gf('django.db.models.fields.URLField')(max_length=255)),
            ('diablo_version', self.gf('django.db.models.fields.CharField')(default=u'2.0.4', max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('youtube', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal(u'core', ['Build'])


    def backwards(self, orm):
        # Deleting model 'Build'
        db.delete_table(u'core_build')


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
            'profile_url': ('django.db.models.fields.URLField', [], {'max_length': '255'}),
            'youtube': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['core']