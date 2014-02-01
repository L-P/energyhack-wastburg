# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'EnergyDay.velec'
        db.add_column(u'wastburg_energyday', 'velec',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'EnergyDay.velec'
        db.delete_column(u'wastburg_energyday', 'velec')


    models = {
        u'wastburg.building': {
            'Meta': {'object_name': 'Building'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'prog': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'wastburg.energyday': {
            'Meta': {'unique_together': "(('lot', 'day'),)", 'object_name': 'EnergyDay'},
            'autre': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'chauffage': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'day': ('django.db.models.fields.DateField', [], {}),
            'ecl': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'ecs': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'elec': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'enr_prod': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lot': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['wastburg.Lot']"}),
            'refroid': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'res_pris': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'temper': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'vecs': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'vef': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'velec': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'ventil': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        u'wastburg.lot': {
            'Meta': {'object_name': 'Lot'},
            'building': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'lots'", 'to': u"orm['wastburg.Building']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        }
    }

    complete_apps = ['wastburg']