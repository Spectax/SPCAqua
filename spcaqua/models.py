from django.db import models

from utils import today, purchase_bill_number, company_bill_number


class Bill(models.Model):

    date = models.DateField("bill date", default=today, db_index=True, blank=False)
    name = models.CharField("name", blank=False, max_length=50)
    place = models.CharField("place", blank=True, max_length=50)

    total_quantity = models.DecimalField("total quantity", max_digits=10, decimal_places=3, blank=False)
    total_price = models.DecimalField("total price", max_digits=10, decimal_places=3, blank=False)

    class Meta:
        abstract = True
    
    def __unicode__(self):
        return u'%s' % (self.bill_no)


class PurchaseBill(Bill):
    
    bill_no = models.CharField("purchase bill number", blank=False, unique=True, default=purchase_bill_number, max_length=12)


class CompanyBill(Bill):

    bill_no = models.CharField("company bill number", blank=False, unique=True, default=company_bill_number, max_length=12)


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
