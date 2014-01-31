# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'EnergyDay'
        db.create_table(u'wastburg_energyday', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lot', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['wastburg.Lot'])),
            ('chauffage', self.gf('django.db.models.fields.FloatField')(blank=True)),
            ('ecs', self.gf('django.db.models.fields.FloatField')(blank=True)),
            ('refroid', self.gf('django.db.models.fields.FloatField')(blank=True)),
            ('ventil', self.gf('django.db.models.fields.FloatField')(blank=True)),
            ('ecl', self.gf('django.db.models.fields.FloatField')(blank=True)),
            ('res_pris', self.gf('django.db.models.fields.FloatField')(blank=True)),
            ('autre', self.gf('django.db.models.fields.FloatField')(blank=True)),
            ('temper', self.gf('django.db.models.fields.FloatField')(blank=True)),
            ('vecs', self.gf('django.db.models.fields.FloatField')(blank=True)),
            ('elec', self.gf('django.db.models.fields.FloatField')(blank=True)),
            ('vef', self.gf('django.db.models.fields.FloatField')(blank=True)),
            ('enr_prod', self.gf('django.db.models.fields.FloatField')(blank=True)),
        ))
        db.send_create_signal(u'wastburg', ['EnergyDay'])


    def backwards(self, orm):
        # Deleting model 'EnergyDay'
        db.delete_table(u'wastburg_energyday')


    models = {
        u'wastburg.building': {
            'Meta': {'object_name': 'Building'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'prog': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'wastburg.energyday': {
            'Meta': {'object_name': 'EnergyDay'},
            'autre': ('django.db.models.fields.FloatField', [], {'blank': 'True'}),
            'chauffage': ('django.db.models.fields.FloatField', [], {'blank': 'True'}),
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