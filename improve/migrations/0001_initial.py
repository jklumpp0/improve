# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Person'
        db.create_table(u'improve_person', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'improve', ['Person'])

        # Adding model 'MetricType'
        db.create_table(u'improve_metrictype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('metric_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('metric_unit', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal(u'improve', ['MetricType'])

        # Adding model 'Condition'
        db.create_table(u'improve_condition', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['improve.Person'])),
            ('metric', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['improve.MetricType'])),
            ('metric_value', self.gf('django.db.models.fields.IntegerField')()),
            ('datetime', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'improve', ['Condition'])


    def backwards(self, orm):
        # Deleting model 'Person'
        db.delete_table(u'improve_person')

        # Deleting model 'MetricType'
        db.delete_table(u'improve_metrictype')

        # Deleting model 'Condition'
        db.delete_table(u'improve_condition')


    models = {
        u'improve.condition': {
            'Meta': {'object_name': 'Condition'},
            'datetime': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
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