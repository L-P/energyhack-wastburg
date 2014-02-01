# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'DjuDay.average'
        db.add_column(u'wastburg_djuday', 'average',
                      self.gf('django.db.models.fields.FloatField')(null=True),
                      keep_default=False)

        # Adding field 'DjuDay.diff'
        db.add_column(u'wastburg_djuday', 'diff',
                      self.gf('django.db.models.fields.FloatField')(null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'DjuDay.average'
        db.delete_column(u'wastburg_djuday', 'average')

        # Deleting field 'DjuDay.diff'
        db.delete_column(u'wastburg_djuday', 'diff')


    models = {
        u'wastburg.building': {
            'Meta': {'object_name': 'Building'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'prog': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'wastburg.buildingfloor': {
            'Meta': {'unique_together': "(('building', 'floor'),)", 'object_name': 'BuildingFloor'},
            'building': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['wastburg.Building']"}),
            'floor': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'wastburg.djuday': {
            'Meta': {'object_name': 'DjuDay'},
            'average': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'day': ('django.db.models.fields.DateField', [], {'unique': 'True'}),
            'diff': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'dju': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'wastburg.energyday': {
            'Meta': {'unique_together': "(('lot', 'day'),)", 'object_name': 'EnergyDay'},
            'day': ('django.db.models.fields.DateField', [], {}),
            'elec': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lot': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'days'", 'to': u"orm['wastburg.Lot']"}),
            'temper': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'vecs': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'vef': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        u'wastburg.lot': {
            'Meta': {'object_name': 'Lot'},
            'building': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'lots'", 'to': u"orm['wastburg.Building']"}),
            'floor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['wastburg.BuildingFloor']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'price': ('django.db.models.fields.FloatField', [], {}),
            'rooms': ('django.db.models.fields.IntegerField', [], {}),
            'surface': ('django.db.models.fields.FloatField', [], {})
        }
    }

    complete_apps = ['wastburg']