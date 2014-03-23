# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'New'
        db.create_table(u'contents_new', (
            (u'content_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['contents.Content'], unique=True, primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('lat', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('lon', self.gf('django.db.models.fields.IntegerField')(max_length=50)),
        ))
        db.send_create_signal(u'contents', ['New'])


    def backwards(self, orm):
        # Deleting model 'New'
        db.delete_table(u'contents_new')


    models = {
        u'contents.content': {
            'Meta': {'object_name': 'Content'},
            'description': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contents.Tag']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contents.new': {
            'Meta': {'object_name': 'New', '_ormbases': [u'contents.Content']},
            u'content_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['contents.Content']", 'unique': 'True', 'primary_key': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'lat': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lon': ('django.db.models.fields.IntegerField', [], {'max_length': '50'})
        },
        u'contents.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        }
    }

    complete_apps = ['contents']