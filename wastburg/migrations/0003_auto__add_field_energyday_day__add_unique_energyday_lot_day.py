# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'EnergyDay.day'
        db.add_column(u'wastburg_energyday', 'day',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 1, 31, 0, 0)),
                      keep_default=False)

        # Adding unique constraint on 'EnergyDay', fields ['lot', 'day']
        db.create_unique(u'wastburg_energyday', ['lot_id', 'day'])


    def backwards(self, orm):
        # Removing unique constraint on 'EnergyDay', fields ['lot', 'day']
        db.delete_unique(u'wastburg_energyday', ['lot_id', 'day'])

        # Deleting field 'EnergyDay.day'
        db.delete_column(u'wastburg_energyday', 'day')


    models = {
        u'wastburg.building': {
            'Meta': {'object_name': 'Building'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'prog': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'wastburg.energyday': {
            'Meta': {'unique_together': "(('lot', 'day'),)", 'object_name': 'EnergyDay'},
            'autre': ('django.db.models.fields.FloatField', [], {'blank': 'True'}),
            'chauffage': ('django.db.models.fields.FloatField', [], {'blank': 'True'}),
            'day': ('django.db.models.fields.DateField', [], {}),
            'ecl': ('django.db.models.fields.FloatField', [], {'blank': 'True'}),
            'ecs': ('django.db.models.fields.FloatField', [], {'blank': 'True'}),
            'elec': ('django.db.models.fields.FloatField', [], {'blank': 'True'}),
            'enr_prod': ('django.db.models.fields.FloatField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lot': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['wastburg.Lot']"}),
            'refroid': ('django.db.models.fields.FloatField', [], {'blank': 'True'}),
            'res_pris': ('django.db.models.fields.FloatField', [], {'blank': 'True'}),
            'temper': ('django.db.models.fields.FloatField', [], {'blank': 'True'}),
            'vecs': ('django.db.models.fields.FloatField', [], {'blank': 'True'}),
            'vef': ('django.db.models.fields.FloatField', [], {'blank': 'True'}),
            'ventil': ('django.db.models.fields.FloatField', [], {'blank': 'True'})
        },
        u'wastburg.lot': {
            'Meta': {'object_name': 'Lot'},
            'building': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['wastburg.Building']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        }
    }

    complete_apps = ['wastburg']