# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Content.title'
        db.alter_column(u'contents_content', 'title', self.gf('django.db.models.fields.CharField')(max_length=60))

        # Changing field 'Content.tag'
        db.alter_column(u'contents_content', 'tag_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contents.Tag'], null=True))

    def backwards(self, orm):

        # Changing field 'Content.title'
        db.alter_column(u'contents_content', 'title', self.gf('django.db.models.fields.CharField')(max_length=50))

        # User chose to not deal with backwards NULL issues for 'Content.tag'
        raise RuntimeError("Cannot reverse this migration. 'Content.tag' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Content.tag'
        db.alter_column(u'contents_content', 'tag_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contents.Tag']))

    models = {
        u'contents.agenda': {
            'Meta': {'object_name': 'Agenda', '_ormbases': [u'contents.Content']},
            u'content_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['contents.Content']", 'unique': 'True', 'primary_key': 'True'}),
            'lat': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'lon': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        u'contents.content': {
            'Meta': {'object_name': 'Content'},
            'description': ('django.db.models.fields.TextField', [], {'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contents.Tag']", 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        u'contents.new': {
            'Meta': {'object_name': 'New', '_ormbases': [u'contents.Content']},
            u'content_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['contents.Content']", 'unique': 'True', 'primary_key': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'lat': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'lon': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        u'contents.place': {
            'Meta': {'object_name': 'Place', '_ormbases': [u'contents.Content']},
            u'content_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['contents.Content']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'contents.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        }
    }

    complete_apps = ['contents']