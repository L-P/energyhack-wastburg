# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'BuildingFloor'
        db.create_table(u'wastburg_buildingfloor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('building', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['wastburg.Building'])),
            ('floor', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'wastburg', ['BuildingFloor'])

        # Adding unique constraint on 'BuildingFloor', fields ['building', 'floor']
        db.create_unique(u'wastburg_buildingfloor', ['building_id', 'floor'])

        # Adding field 'Lot.floor'
        db.add_column(u'wastburg_lot', 'floor',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['wastburg.BuildingFloor']),
                      keep_default=False)

        # Adding field 'Lot.rooms'
        db.add_column(u'wastburg_lot', 'rooms',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)

        # Adding field 'Lot.surface'
        db.add_column(u'wastburg_lot', 'surface',
                      self.gf('django.db.models.fields.FloatField')(default=20),
                      keep_default=False)

        # Adding field 'Lot.price'
        db.add_column(u'wastburg_lot', 'price',
                      self.gf('django.db.models.fields.FloatField')(default=100),
                      keep_default=False)


    def backwards(self, orm):
        # Removing unique constraint on 'BuildingFloor', fields ['building', 'floor']
        db.delete_unique(u'wastburg_buildingfloor', ['building_id', 'floor'])

        # Deleting model 'BuildingFloor'
        db.delete_table(u'wastburg_buildingfloor')

        # Deleting field 'Lot.floor'
        db.delete_column(u'wastburg_lot', 'floor_id')

        # Deleting field 'Lot.rooms'
        db.delete_column(u'wastburg_lot', 'rooms')

        # Deleting field 'Lot.surface'
        db.delete_column(u'wastburg_lot', 'surface')

        # Deleting field 'Lot.price'
        db.delete_column(u'wastburg_lot', 'price')


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