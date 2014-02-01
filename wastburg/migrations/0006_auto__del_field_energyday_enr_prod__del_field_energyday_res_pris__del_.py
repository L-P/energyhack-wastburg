# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'EnergyDay.enr_prod'
        db.delete_column(u'wastburg_energyday', 'enr_prod')

        # Deleting field 'EnergyDay.res_pris'
        db.delete_column(u'wastburg_energyday', 'res_pris')

        # Deleting field 'EnergyDay.chauffage'
        db.delete_column(u'wastburg_energyday', 'chauffage')

        # Deleting field 'EnergyDay.ecl'
        db.delete_column(u'wastburg_energyday', 'ecl')

        # Deleting field 'EnergyDay.velec'
        db.delete_column(u'wastburg_energyday', 'velec')

        # Deleting field 'EnergyDay.refroid'
        db.delete_column(u'wastburg_energyday', 'refroid')

        # Deleting field 'EnergyDay.autre'
        db.delete_column(u'wastburg_energyday', 'autre')

        # Deleting field 'EnergyDay.ecs'
        db.delete_column(u'wastburg_energyday', 'ecs')

        # Deleting field 'EnergyDay.ventil'
        db.delete_column(u'wastburg_energyday', 'ventil')


    def backwards(self, orm):
        # Adding field 'EnergyDay.enr_prod'
        db.add_column(u'wastburg_energyday', 'enr_prod',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'EnergyDay.res_pris'
        db.add_column(u'wastburg_energyday', 'res_pris',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'EnergyDay.chauffage'
        db.add_column(u'wastburg_energyday', 'chauffage',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'EnergyDay.ecl'
        db.add_column(u'wastburg_energyday', 'ecl',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'EnergyDay.velec'
        db.add_column(u'wastburg_energyday', 'velec',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'EnergyDay.refroid'
        db.add_column(u'wastburg_energyday', 'refroid',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'EnergyDay.autre'
        db.add_column(u'wastburg_energyday', 'autre',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'EnergyDay.ecs'
        db.add_column(u'wastburg_energyday', 'ecs',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'EnergyDay.ventil'
        db.add_column(u'wastburg_energyday', 'ventil',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)


    models = {
        u'wastburg.building': {
            'Meta': {'object_name': 'Building'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'prog': ('django.db.models.fields.CharField', [], {'max_length': '50'})
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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        }
    }

    complete_apps = ['wastburg']