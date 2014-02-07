# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PurchaseBill'
        db.create_table(u'spcaqua_purchasebill', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 2, 7, 0, 0), db_index=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('place', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 2, 7, 0, 0), db_index=True)),
            ('total_quantity', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=3)),
            ('total_price', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=3)),
            ('bill_no', self.gf('django.db.models.fields.CharField')(default='1070214P', unique=True, max_length=12)),
        ))
        db.send_create_signal(u'spcaqua', ['PurchaseBill'])

        # Adding model 'CompanyBill'
        db.create_table(u'spcaqua_companybill', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 2, 7, 0, 0), db_index=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('place', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 2, 7, 0, 0), db_index=True)),
            ('total_quantity', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=3)),
            ('total_price', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=3)),
            ('bill_no', self.gf('django.db.models.fields.CharField')(default='1070214C', unique=True, max_length=12)),
        ))
        db.send_create_signal(u'spcaqua', ['CompanyBill'])

        # Adding model 'PurchaseBillContent'
        db.create_table(u'spcaqua_purchasebillcontent', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('s_no', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('count', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('quantity', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=3)),
            ('rate', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=3)),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=3)),
            ('purchase_bill', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['spcaqua.PurchaseBill'])),
        ))
        db.send_create_signal(u'spcaqua', ['PurchaseBillContent'])

        # Adding model 'CompanyBillContent'
        db.create_table(u'spcaqua_companybillcontent', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('s_no', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('count', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('quantity', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=3)),
            ('rate', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=3)),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=3)),
            ('company_bill', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['spcaqua.CompanyBill'])),
        ))
        db.send_create_signal(u'spcaqua', ['CompanyBillContent'])

        # Adding model 'Lot'
        db.create_table(u'spcaqua_lot', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lot_no', self.gf('django.db.models.fields.CharField')(default='1070214L', unique=True, max_length=12)),
            ('date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 2, 7, 0, 0), db_index=True)),
            ('company_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('company_address', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('total_quantity', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=3)),
            ('vehicle_number', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('seal_number', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('driver_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('driver_phone', self.gf('django.db.models.fields.CharField')(max_length=12)),
            ('created_at', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 2, 7, 0, 0), db_index=True)),
        ))
        db.send_create_signal(u'spcaqua', ['Lot'])

        # Adding model 'LotContent'
        db.create_table(u'spcaqua_lotcontent', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('s_no', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('count', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('quantity', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=3)),
            ('no_of_boxes_with_identifier', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('lot', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['spcaqua.Lot'])),
        ))
        db.send_create_signal(u'spcaqua', ['LotContent'])

        # Adding model 'IceBill'
        db.create_table(u'spcaqua_icebill', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('bill_no', self.gf('django.db.models.fields.CharField')(default='1070214I', unique=True, max_length=12)),
            ('date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 2, 7, 0, 0), db_index=True)),
            ('company_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('company_address', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('created_at', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 2, 7, 0, 0), db_index=True)),
        ))
        db.send_create_signal(u'spcaqua', ['IceBill'])

        # Adding model 'IceBillContent'
        db.create_table(u'spcaqua_icebillcontent', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('s_no', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('no_of_cans', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=3)),
            ('rate', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=3)),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=3)),
            ('ice_bill', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['spcaqua.IceBill'])),
        ))
        db.send_create_signal(u'spcaqua', ['IceBillContent'])


    def backwards(self, orm):
        # Deleting model 'PurchaseBill'
        db.delete_table(u'spcaqua_purchasebill')

        # Deleting model 'CompanyBill'
        db.delete_table(u'spcaqua_companybill')

        # Deleting model 'PurchaseBillContent'
        db.delete_table(u'spcaqua_purchasebillcontent')

        # Deleting model 'CompanyBillContent'
        db.delete_table(u'spcaqua_companybillcontent')

        # Deleting model 'Lot'
        db.delete_table(u'spcaqua_lot')

        # Deleting model 'LotContent'
        db.delete_table(u'spcaqua_lotcontent')

        # Deleting model 'IceBill'
        db.delete_table(u'spcaqua_icebill')

        # Deleting model 'IceBillContent'
        db.delete_table(u'spcaqua_icebillcontent')


    models = {
        u'spcaqua.companybill': {
            'Meta': {'ordering': "['-created_at']", 'object_name': 'CompanyBill'},
            'bill_no': ('django.db.models.fields.CharField', [], {'default': "'1070214C'", 'unique': 'True', 'max_length': '12'}),
            'created_at': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 2, 7, 0, 0)', 'db_index': 'True'}),
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
            'created_at': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 2, 7, 0, 0)', 'db_index': 'True'}),
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
            'created_at': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 2, 7, 0, 0)', 'db_index': 'True'}),
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
            'created_at': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 2, 7, 0, 0)', 'db_index': 'True'}),
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