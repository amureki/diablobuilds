# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'FAQ'
        db.create_table(u'core_faq', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('answer', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'core', ['FAQ'])


    def backwards(self, orm):
        # Deleting model 'FAQ'
        db.delete_table(u'core_faq')


    models = {
        u'core.build': {
            'Meta': {'ordering': "(u'-diablo_version', u'-rating')", 'object_name': 'Build'},
            'author': ('django.db.models.fields.CharField', [], {'default': "u'\\u0413\\u043e\\u0441\\u0442\\u044c'", 'max_length': '255'}),
            'calculator_url': ('django.db.models.fields.URLField', [], {'max_length': '255'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'diablo_version': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Version']", 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '255'}),
            'hero_class': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'profile_url': ('django.db.models.fields.URLField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'rating': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'youtube': ('django.db.models.fields.URLField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'core.faq': {
            'Meta': {'object_name': 'FAQ'},
            'answer': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'core.guest': {
            'Meta': {'ordering': "(u'ip',)", 'object_name': 'Guest'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.CharField', [], {'default': '0', 'max_length': '255'}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'rated_builds': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['core.Build']", 'null': 'True', 'through': u"orm['core.Vote']", 'blank': 'True'}),
            'referer': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'user_agent': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'core.news': {
            'Meta': {'ordering': "(u'-id',)", 'object_name': 'News'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 10, 28, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'core.version': {
            'Meta': {'object_name': 'Version'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "u'2.1.0'", 'max_length': '255'})
        },
        u'core.vote': {
            'Meta': {'object_name': 'Vote'},
            'action': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'build': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Build']"}),
            'date_voted': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'guest': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Guest']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['core']