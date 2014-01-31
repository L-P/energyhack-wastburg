# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Building'
        db.create_table(u'wastburg_building', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('prog', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'wastburg', ['Building'])

        # Adding model 'Lot'
        db.create_table(u'wastburg_lot', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('building', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['wastburg.Building'])),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
        ))
        db.send_create_signal(u'wastburg', ['Lot'])


    def backwards(self, orm):
        # Deleting model 'Building'
        db.delete_table(u'wastburg_building')

        # Deleting model 'Lot'
        db.delete_table(u'wastburg_lot')


    models = {
        u'wastburg.building': {
            'Meta': {'object_name': 'Building'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'prog': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'wastburg.lot': {
            'Meta': {'object_name': 'Lot'},
            'building': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['wastburg.Building']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        }
    }

    complete_apps = ['wastburg']