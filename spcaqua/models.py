from django.db import models

from utils import today


class Bill(models.Model):

    date = models.DateField("bill date", default=today, db_index=True, blank=False)
    name = models.CharField("name", blank=False, max_length=50)
    place = models.CharField("place", blank=True, max_length=50)

    total_quantity = models.DecimalField("total quantity", max_digits=10, decimal_places=3, blank=False)
    total_price = models.DecimalField("total price", max_digits=10, decimal_places=3, blank=False)
    total_price_words = models.CharField("total price in words", max_length=100, blank=True)

    class Meta:
        abstract = True


class PurchaseBill(Bill):
    
    bill_no = models.CharField("purchase bill number", blank=False, unique=True, max_length=12)

    def save(self, *args, **kwargs):
        total_bills_today = PurchaseBill.objects.filter(date=today).count()
        date_string = today().strftime("%d-%m-%y")
        date = date_string.split("-")
        day = date[0]
        month = date[1]
        year = date[2]
        self.bill_no = str(total_bills_today + 1) + day + month + year + "P"
        return super(PurchaseBill, self).save(*args, **kwargs)


class CompanyBill(Bill):

    bill_no = models.CharField("company bill number", blank=False, unique=True, max_length=12)

    def save(self, *args, **kwargs):
        total_bills_today = CompanyBill.objects.filter(date=today).count()
        date_string = today().strftime("%d-%m-%y")
        date = date_string.split("-")
        day = date[0]
        month = date[1]
        year = date[2]
        self.bill_no = str(total_bills_today + 1) + day + month + year + "C"
        return super(CompanyBill, self).save(*args, **kwargs)


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
