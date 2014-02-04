from django.db import models

from utils import today, purchase_bill_number, company_bill_number, lot_number, ice_bill_number


class Bill(models.Model):

    date = models.DateField("bill date", default=today, db_index=True, blank=False)
    name = models.CharField("name", blank=False, max_length=50)
    place = models.CharField("place", blank=True, max_length=50)
    
    created_at = models.DateField("bill creation date", default=today, db_index=True, blank=False)

    total_quantity = models.DecimalField("total quantity", max_digits=10, decimal_places=3, blank=False)
    total_price = models.DecimalField("total price", max_digits=10, decimal_places=3, blank=False)

    class Meta:
        abstract = True
    
    def __unicode__(self):
        return u'%s' % (self.bill_no)


class PurchaseBill(Bill):
    
    bill_no = models.CharField("purchase bill number", blank=False, unique=True, default=purchase_bill_number, max_length=12)

    class Meta:
        ordering = ["created_at"]


class CompanyBill(Bill):

    bill_no = models.CharField("company bill number", blank=False, unique=True, default=company_bill_number, max_length=12)

    class Meta:
        ordering = ["created_at"]


class BillContent(models.Model):

    s_no = models.CharField("S.No.", blank=False, max_length=3)
    count = models.CharField("Count", blank=False, max_length=8)
    quantity = models.DecimalField("Quantity", blank=False, max_digits=8, decimal_places=3)
    rate = models.DecimalField("Rate", blank=False, max_digits=8, decimal_places=3)
    price = models.DecimalField("Price", blank=False, max_digits=10, decimal_places=3)

    class Meta:
        abstract = True


class PurchaseBillContent(BillContent):

    purchase_bill = models.ForeignKey(PurchaseBill)


class CompanyBillContent(BillContent):

    company_bill = models.ForeignKey(CompanyBill)


class Lot(models.Model):

    lot_no = models.CharField("Lot No", blank=False, unique=True, default=lot_number, max_length=12)
    date = models.DateField("lot date", default=today, db_index=True, blank=False)
    company_name = models.CharField("company name", blank=False, max_length=50)
    company_address = models.CharField("company address", blank=False, max_length=50)

    total_quantity = models.DecimalField("total quantity", max_digits=15, decimal_places=3, blank=False)

    vehicle_number = models.CharField("vehicle number", blank=False, max_length=15)
    seal_number = models.CharField("seal number", blank=False, max_length=15)

    driver_name = models.CharField("driver name", blank=False, max_length=50)
    driver_phone = models.CharField("driver phone number", blank=False, max_length=12)
    
    created_at = models.DateField("Lot creation date", default=today, db_index=True, blank=False)
    
    def __unicode__(self):
        return u'%s' % (self.lot_no)

    class Meta:
        ordering = ["created_at"]


class LotContent(models.Model):

    s_no = models.CharField("S.No.", blank=False, max_length=3)
    count = models.CharField("Count", blank=False, max_length=8)
    quantity = models.DecimalField("Quantity", blank=False, max_digits=10, decimal_places=3)
    no_of_boxes_with_identifier = models.CharField("Number of boxes with identifier", blank=False, max_length=10)
    lot = models.ForeignKey(Lot)


class IceBill(models.Model):

    bill_no = models.CharField("Bill No", blank=False, unique=True, default=ice_bill_number, max_length=12)
    date = models.DateField("lot date", default=today, db_index=True, blank=False)
    company_name = models.CharField("company name", blank=False, max_length=50)
    company_address = models.CharField("company address", blank=False, max_length=50)
    
    created_at = models.DateField("bill creation date", default=today, db_index=True, blank=False)
    
    def __unicode__(self):
        return u'%s' % (self.bill_no)

    class Meta:
        ordering = ["created_at"]

        
class IceBillContent(models.Model):

    s_no = models.CharField("S.No.", blank=False, max_length=3)
    no_of_cans = models.DecimalField("Number of Cans", blank=False, max_digits=10, decimal_places=3)
    rate = models.DecimalField("Rate", blank=False, max_digits=8, decimal_places=3)
    price = models.DecimalField("Price", blank=False, max_digits=10, decimal_places=3)
    ice_bill = models.ForeignKey(IceBill)
