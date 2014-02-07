from django.utils.timezone import now, localtime

import spcaqua


def today():
    return localtime(now())


def purchase_bill_number():
    bills_today = spcaqua.models.PurchaseBill.objects.filter(created_at=today)
    if not bills_today:
        total_bills_today = 0
    else:
        total_bills_today = int(bills_today[0].bill_no[:-7])
    date_string = today().strftime("%d-%m-%y")
    date = date_string.split("-")
    day = date[0]
    month = date[1]
    year = date[2]
    bill_no = str(total_bills_today + 1) + day + month + year + "P"
    return bill_no


def company_bill_number():
    bills_today = spcaqua.models.CompanyBill.objects.filter(created_at=today)
    if not bills_today:
        total_bills_today = 0
    else:
        total_bills_today = int(bills_today[0].bill_no[:-7])
    date_string = today().strftime("%d-%m-%y")
    date = date_string.split("-")
    day = date[0]
    month = date[1]
    year = date[2]
    bill_no = str(total_bills_today + 1) + day + month + year + "C"
    return bill_no


def lot_number():
    lots_today = spcaqua.models.Lot.objects.filter(created_at=today)
    if not lots_today:
        total_lots_today = 0
    else:
        total_lots_today = int(lots_today[0].lot_no[:-7])
    date_string = today().strftime("%d-%m-%y")
    date = date_string.split("-")
    day = date[0]
    month = date[1]
    year = date[2]
    lot_no = str(total_lots_today + 1) + day + month + year + "L"
    return lot_no

    
def ice_bill_number():
    bills_today = spcaqua.models.IceBill.objects.filter(created_at=today)
    if not bills_today:
        total_bills_today = 0
    else:
        total_bills_today = int(bills_today[0].bill_no[:-7])
    date_string = today().strftime("%d-%m-%y")
    date = date_string.split("-")
    day = date[0]
    month = date[1]
    year = date[2]
    bill_no = str(total_bills_today + 1) + day + month + year + "I"
    return bill_no
