from django.utils.timezone import now, localtime

import spcaqua


def today():
    return localtime(now()).date()


def purchase_bill_number():
    total_bills_today = spcaqua.models.PurchaseBill.objects.filter(date=today).count()
    date_string = today().strftime("%d-%m-%y")
    date = date_string.split("-")
    day = date[0]
    month = date[1]
    year = date[2]
    bill_no = str(total_bills_today + 1) + day + month + year + "P"
    return bill_no


def company_bill_number():
    total_bills_today = spcaqua.models.CompanyBill.objects.filter(date=today).count()
    date_string = today().strftime("%d-%m-%y")
    date = date_string.split("-")
    day = date[0]
    month = date[1]
    year = date[2]
    bill_no = str(total_bills_today + 1) + day + month + year + "C"
    return bill_no


def lot_number():
    total_lots_today = spcaqua.models.Lot.objects.filter(date=today).count()
    date_string = today().strftime("%d-%m-%y")
    date = date_string.split("-")
    day = date[0]
    month = date[1]
    year = date[2]
    lot_no = str(total_lots_today + 1) + day + month + year + "L"
    return lot_no

    
def ice_bill_number():
    total_bills_today = spcaqua.models.IceBill.objects.filter(date=today).count()
    date_string = today().strftime("%d-%m-%y")
    date = date_string.split("-")
    day = date[0]
    month = date[1]
    year = date[2]
    bill_no = str(total_bills_today + 1) + day + month + year + "I"
    return bill_no