# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Condition.datetime'
        db.delete_column(u'improve_condition', 'datetime')

        # Adding field 'Condition.date'
        db.add_column(u'improve_condition', 'date',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2013, 8, 26, 0, 0), blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Condition.datetime'
        db.add_column(u'improve_condition', 'datetime',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=0, blank=True),
                      keep_default=False)

        # Deleting field 'Condition.date'
        db.delete_column(u'improve_condition', 'date')


    models = {
        u'improve.condition': {
            'Meta': {'object_name': 'Condition'},
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'metric': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['improve.MetricType']"}),
            'metric_value': ('django.db.models.fields.IntegerField', [], {}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['improve.Person']"})
        },
        u'improve.metrictype': {
            'Meta': {'object_name': 'MetricType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'metric_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'metric_unit': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        u'improve.person': {
            'Meta': {'object_name': 'Person'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['improve']