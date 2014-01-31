# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'EnergyDay.autre'
        db.alter_column(u'wastburg_energyday', 'autre', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'EnergyDay.res_pris'
        db.alter_column(u'wastburg_energyday', 'res_pris', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'EnergyDay.chauffage'
        db.alter_column(u'wastburg_energyday', 'chauffage', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'EnergyDay.ecl'
        db.alter_column(u'wastburg_energyday', 'ecl', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'EnergyDay.refroid'
        db.alter_column(u'wastburg_energyday', 'refroid', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'EnergyDay.vef'
        db.alter_column(u'wastburg_energyday', 'vef', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'EnergyDay.elec'
        db.alter_column(u'wastburg_energyday', 'elec', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'EnergyDay.enr_prod'
        db.alter_column(u'wastburg_energyday', 'enr_prod', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'EnergyDay.ecs'
        db.alter_column(u'wastburg_energyday', 'ecs', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'EnergyDay.vecs'
        db.alter_column(u'wastburg_energyday', 'vecs', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'EnergyDay.ventil'
        db.alter_column(u'wastburg_energyday', 'ventil', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'EnergyDay.temper'
        db.alter_column(u'wastburg_energyday', 'temper', self.gf('django.db.models.fields.FloatField')(null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'EnergyDay.autre'
        raise RuntimeError("Cannot reverse this migration. 'EnergyDay.autre' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'EnergyDay.autre'
        db.alter_column(u'wastburg_energyday', 'autre', self.gf('django.db.models.fields.FloatField')())

        # User chose to not deal with backwards NULL issues for 'EnergyDay.res_pris'
        raise RuntimeError("Cannot reverse this migration. 'EnergyDay.res_pris' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'EnergyDay.res_pris'
        db.alter_column(u'wastburg_energyday', 'res_pris', self.gf('django.db.models.fields.FloatField')())

        # User chose to not deal with backwards NULL issues for 'EnergyDay.chauffage'
        raise RuntimeError("Cannot reverse this migration. 'EnergyDay.chauffage' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'EnergyDay.chauffage'
        db.alter_column(u'wastburg_energyday', 'chauffage', self.gf('django.db.models.fields.FloatField')())

        # User chose to not deal with backwards NULL issues for 'EnergyDay.ecl'
        raise RuntimeError("Cannot reverse this migration. 'EnergyDay.ecl' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'EnergyDay.ecl'
        db.alter_column(u'wastburg_energyday', 'ecl', self.gf('django.db.models.fields.FloatField')())

        # User chose to not deal with backwards NULL issues for 'EnergyDay.refroid'
        raise RuntimeError("Cannot reverse this migration. 'EnergyDay.refroid' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'EnergyDay.refroid'
        db.alter_column(u'wastburg_energyday', 'refroid', self.gf('django.db.models.fields.FloatField')())

        # User chose to not deal with backwards NULL issues for 'EnergyDay.vef'
        raise RuntimeError("Cannot reverse this migration. 'EnergyDay.vef' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'EnergyDay.vef'
        db.alter_column(u'wastburg_energyday', 'vef', self.gf('django.db.models.fields.FloatField')())

        # User chose to not deal with backwards NULL issues for 'EnergyDay.elec'
        raise RuntimeError("Cannot reverse this migration. 'EnergyDay.elec' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'EnergyDay.elec'
        db.alter_column(u'wastburg_energyday', 'elec', self.gf('django.db.models.fields.FloatField')())

        # User chose to not deal with backwards NULL issues for 'EnergyDay.enr_prod'
        raise RuntimeError("Cannot reverse this migration. 'EnergyDay.enr_prod' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'EnergyDay.enr_prod'
        db.alter_column(u'wastburg_energyday', 'enr_prod', self.gf('django.db.models.fields.FloatField')())

        # User chose to not deal with backwards NULL issues for 'EnergyDay.ecs'
        raise RuntimeError("Cannot reverse this migration. 'EnergyDay.ecs' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'EnergyDay.ecs'
        db.alter_column(u'wastburg_energyday', 'ecs', self.gf('django.db.models.fields.FloatField')())

        # User chose to not deal with backwards NULL issues for 'EnergyDay.vecs'
        raise RuntimeError("Cannot reverse this migration. 'EnergyDay.vecs' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'EnergyDay.vecs'
        db.alter_column(u'wastburg_energyday', 'vecs', self.gf('django.db.models.fields.FloatField')())

        # User chose to not deal with backwards NULL issues for 'EnergyDay.ventil'
        raise RuntimeError("Cannot reverse this migration. 'EnergyDay.ventil' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'EnergyDay.ventil'
        db.alter_column(u'wastburg_energyday', 'ventil', self.gf('django.db.models.fields.FloatField')())

        # User chose to not deal with backwards NULL issues for 'EnergyDay.temper'
        raise RuntimeError("Cannot reverse this migration. 'EnergyDay.temper' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'EnergyDay.temper'
        db.alter_column(u'wastburg_energyday', 'temper', self.gf('django.db.models.fields.FloatField')())

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
            'ventil': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        u'wastburg.lot': {
            'Meta': {'object_name': 'Lot'},
            'building': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['wastburg.Building']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        }
    }

    complete_apps = ['wastburg']