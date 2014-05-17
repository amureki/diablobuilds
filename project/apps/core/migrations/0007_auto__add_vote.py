# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Vote'
        db.create_table(u'core_vote', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('build', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Build'])),
            ('guest', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Guest'])),
            ('date_voted', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'core', ['Vote'])

        # Removing M2M table for field rated_builds on 'Guest'
        db.delete_table(db.shorten_name(u'core_guest_rated_builds'))


    def backwards(self, orm):
        # Deleting model 'Vote'
        db.delete_table(u'core_vote')

        # Adding M2M table for field rated_builds on 'Guest'
        m2m_table_name = db.shorten_name(u'core_guest_rated_builds')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('guest', models.ForeignKey(orm[u'core.guest'], null=False)),
            ('build', models.ForeignKey(orm[u'core.build'], null=False))
        ))
        db.create_unique(m2m_table_name, ['guest_id', 'build_id'])


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
            'rated_builds': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['core.Build']", 'null': 'True', 'through': u"orm['core.Vote']", 'blank': 'True'}),
            'referrer': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'user_agent': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'core.vote': {
            'Meta': {'object_name': 'Vote'},
            'build': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Build']"}),
            'date_voted': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'guest': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Guest']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['core']