# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Lot.created_at'
        db.alter_column(u'spcaqua_lot', 'created_at', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'CompanyBill.created_at'
        db.alter_column(u'spcaqua_companybill', 'created_at', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'IceBill.created_at'
        db.alter_column(u'spcaqua_icebill', 'created_at', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'PurchaseBill.created_at'
        db.alter_column(u'spcaqua_purchasebill', 'created_at', self.gf('django.db.models.fields.DateTimeField')())

    def backwards(self, orm):

        # Changing field 'Lot.created_at'
        db.alter_column(u'spcaqua_lot', 'created_at', self.gf('django.db.models.fields.DateField')())

        # Changing field 'CompanyBill.created_at'
        db.alter_column(u'spcaqua_companybill', 'created_at', self.gf('django.db.models.fields.DateField')())

        # Changing field 'IceBill.created_at'
        db.alter_column(u'spcaqua_icebill', 'created_at', self.gf('django.db.models.fields.DateField')())

        # Changing field 'PurchaseBill.created_at'
        db.alter_column(u'spcaqua_purchasebill', 'created_at', self.gf('django.db.models.fields.DateField')())

    models = {
        u'spcaqua.companybill': {
            'Meta': {'ordering': "['-created_at']", 'object_name': 'CompanyBill'},
            'bill_no': ('django.db.models.fields.CharField', [], {'default': "'1070214C'", 'unique': 'True', 'max_length': '12'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 2, 7, 0, 0)', 'db_index': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 2, 7, 0, 0)', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'place': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'total_price': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '3'}),
            'total_quantity': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '3'})
        },
        u'spcaqua.companybillcontent': {
            'Meta': {'object_name': 'CompanyBillContent'},
            'company_bill': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['spcaqua.CompanyBill']"}),
            'count': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '3'}),
            'quantity': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '3'}),
            'rate': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '3'}),
            's_no': ('django.db.models.fields.CharField', [], {'max_length': '3'})
        },
        u'spcaqua.icebill': {
            'Meta': {'ordering': "['-created_at']", 'object_name': 'IceBill'},
            'bill_no': ('django.db.models.fields.CharField', [], {'default': "'1070214I'", 'unique': 'True', 'max_length': '12'}),
            'company_address': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'company_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 2, 7, 0, 0)', 'db_index': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 2, 7, 0, 0)', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'spcaqua.icebillcontent': {
            'Meta': {'object_name': 'IceBillContent'},
            'ice_bill': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['spcaqua.IceBill']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'no_of_cans': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '3'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '3'}),
            'rate': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '3'}),
            's_no': ('django.db.models.fields.CharField', [], {'max_length': '3'})
        },
        u'spcaqua.lot': {
            'Meta': {'ordering': "['-created_at']", 'object_name': 'Lot'},
            'company_address': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'company_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 2, 7, 0, 0)', 'db_index': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 2, 7, 0, 0)', 'db_index': 'True'}),
            'driver_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'driver_phone': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lot_no': ('django.db.models.fields.CharField', [], {'default': "'1070214L'", 'unique': 'True', 'max_length': '12'}),
            'seal_number': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'total_quantity': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '3'}),
            'vehicle_number': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        },
        u'spcaqua.lotcontent': {
            'Meta': {'object_name': 'LotContent'},
            'count': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lot': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['spcaqua.Lot']"}),
            'no_of_boxes_with_identifier': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'quantity': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '3'}),
            's_no': ('django.db.models.fields.CharField', [], {'max_length': '3'})
        },
        u'spcaqua.purchasebill': {
            'Meta': {'ordering': "['-created_at']", 'object_name': 'PurchaseBill'},
            'bill_no': ('django.db.models.fields.CharField', [], {'default': "'1070214P'", 'unique': 'True', 'max_length': '12'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 2, 7, 0, 0)', 'db_index': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 2, 7, 0, 0)', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'place': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'total_price': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '3'}),
            'total_quantity': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '3'})
        },
        u'spcaqua.purchasebillcontent': {
            'Meta': {'object_name': 'PurchaseBillContent'},
            'count': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '3'}),
            'purchase_bill': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['spcaqua.PurchaseBill']"}),
            'quantity': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '3'}),
            'rate': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '3'}),
            's_no': ('django.db.models.fields.CharField', [], {'max_length': '3'})
        }
    }

    complete_apps = ['spcaqua']