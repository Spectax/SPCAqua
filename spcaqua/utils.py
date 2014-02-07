from django.utils.timezone import now, localtime, timedelta

from datetime import time, datetime

import spcaqua


def today():
    return localtime(now())


def purchase_bill_number():
    this_day = today()
    next_day = this_day + timedelta(days=1)
    this_day_start = datetime.combine(this_day, time())
    this_day_end = datetime.combine(next_day, time())
    bills_today = spcaqua.models.PurchaseBill.objects.filter(created_at__range=(this_day_start, this_day_end))
    if not bills_today:
        total_bills_today = 0
    else:
        total_bills_today = int(list(bills_today)[-1].bill_no[:-7])
    date_string = today().strftime("%d-%m-%y")
    date = date_string.split("-")
    day = date[0]
    month = date[1]
    year = date[2]
    bill_no = str(total_bills_today + 1) + day + month + year + "P"
    return bill_no


def company_bill_number():
    this_day = today()
    next_day = this_day + timedelta(days=1)
    this_day_start = datetime.combine(this_day, time())
    this_day_end = datetime.combine(next_day, time())
    bills_today = spcaqua.models.CompanyBill.objects.filter(created_at__range=(this_day_start, this_day_end))
    if not bills_today:
        total_bills_today = 0
    else:
        total_bills_today = int(list(bills_today)[-1].bill_no[:-7])
    date_string = today().strftime("%d-%m-%y")
    date = date_string.split("-")
    day = date[0]
    month = date[1]
    year = date[2]
    bill_no = str(total_bills_today + 1) + day + month + year + "C"
    return bill_no


def lot_number():
    this_day = today()
    next_day = this_day + timedelta(days=1)
    this_day_start = datetime.combine(this_day, time())
    this_day_end = datetime.combine(next_day, time())
    lots_today = spcaqua.models.Lot.objects.filter(created_at__range=(this_day_start, this_day_end))
    if not lots_today:
        total_lots_today = 0
    else:
        total_lots_today = int(list(lots_today)[-1].lot_no[:-7])
    date_string = today().strftime("%d-%m-%y")
    date = date_string.split("-")
    day = date[0]
    month = date[1]
    year = date[2]
    lot_no = str(total_lots_today + 1) + day + month + year + "L"
    return lot_no

    
def ice_bill_number():
    this_day = today()
    next_day = this_day + timedelta(days=1)
    this_day_start = datetime.combine(this_day, time())
    this_day_end = datetime.combine(next_day, time())
    bills_today = spcaqua.models.IceBill.objects.filter(created_at__range=(this_day_start, this_day_end))
    if not bills_today:
        total_bills_today = 0
    else:
        total_bills_today = int(list(bills_today)[-1].bill_no[:-7])
    date_string = today().strftime("%d-%m-%y")
    date = date_string.split("-")
    day = date[0]
    month = date[1]
    year = date[2]
    bill_no = str(total_bills_today + 1) + day + month + year + "I"
    return bill_no
