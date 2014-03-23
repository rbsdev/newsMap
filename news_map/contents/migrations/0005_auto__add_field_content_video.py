# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Content.video'
        db.add_column(u'contents_content', 'video',
                      self.gf('django.db.models.fields.TextField')(max_length=300, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Content.video'
        db.delete_column(u'contents_content', 'video')


    models = {
        u'contents.agenda': {
            'Meta': {'object_name': 'Agenda', '_ormbases': [u'contents.Content']},
            u'content_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['contents.Content']", 'unique': 'True', 'primary_key': 'True'}),
            'lat': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'lon': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'})
        },
        u'contents.content': {
            'Meta': {'object_name': 'Content'},
            'description': ('django.db.models.fields.TextField', [], {'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contents.Tag']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'video': ('django.db.models.fields.TextField', [], {'max_length': '300', 'null': 'True'})
        },
        u'contents.new': {
            'Meta': {'object_name': 'New', '_ormbases': [u'contents.Content']},
            u'content_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['contents.Content']", 'unique': 'True', 'primary_key': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'lat': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'lon': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'})
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