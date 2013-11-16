from django.contrib import admin
from models import PurchaseBill, CompanyBill, PurchaseBillContent, CompanyBillContent, Lot, LotContent, IceBill, IceBillContent

admin.site.register(PurchaseBill)
admin.site.register(CompanyBill)
admin.site.register(PurchaseBillContent)
admin.site.register(CompanyBillContent)
admin.site.register(Lot)
admin.site.register(LotContent)
admin.site.register(IceBill)
admin.site.register(IceBillContent)