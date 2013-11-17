from django import forms

from spcaqua.models import (
    CompanyBill,
    PurchaseBill,
    CompanyBillContent,
    PurchaseBillContent,
    Lot,
    LotContent,
    IceBill,
    IceBillContent,
)
from utils import today


class CompanyBillForm(forms.ModelForm):

    date = forms.DateField(initial=today, widget=forms.DateInput(format="%d/%m/%Y"), input_formats=("%d/%m/%Y",))

    class Meta:
        model = CompanyBill
        exclude = ("total_price", "total_quantity", "created_at")
        widgets = {
            "bill_no": forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super(CompanyBillForm, self).__init__(*args, **kwargs)
        self.fields.keyOrder = [
            "bill_no",
            "name",
            "place",
            "date"
        ]


class CompanyBillContentForm(forms.ModelForm):

    class Meta:
        model = CompanyBillContent
        exclude = ("company_bill",)


class PurchaseBillForm(forms.ModelForm):

    date = forms.DateField(initial=today, widget=forms.DateInput(format="%d/%m/%Y"), input_formats=("%d/%m/%Y",))

    class Meta:
        model = PurchaseBill
        exclude = ("total_price", "total_quantity", "created_at")
        widgets = {
            "bill_no": forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super(PurchaseBillForm, self).__init__(*args, **kwargs)
        self.fields.keyOrder = [
            "bill_no",
            "name",
            "place",
            "date"
        ]


class PurchaseBillContentForm(forms.ModelForm):

    class Meta:
        model = PurchaseBillContent
        exclude = ("purchase_bill",)


class LotForm(forms.ModelForm):

    date = forms.DateField(initial=today, widget=forms.DateInput(format="%d/%m/%Y"), input_formats=("%d/%m/%Y",))

    class Meta:
        model = Lot
        exclude= ("total_quantity", "created_at")
        widgets = {
            "lot_no": forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super(LotForm, self).__init__(*args, **kwargs)
        self.fields.keyOrder = [
            "lot_no",
            "company_name",
            "company_address",
            "vehicle_number",
            "seal_number",
            "driver_name",
            "driver_phone",
            "date"
        ]


class LotContentForm(forms.ModelForm):

    class Meta:
        model = LotContent
        exclude = ("lot",)


class IceBillForm(forms.ModelForm):

    date = forms.DateField(initial=today, widget=forms.DateInput(format="%d/%m/%Y"), input_formats=("%d/%m/%Y",))

    class Meta:
        model = IceBill
        exclude= ("created_at")
        widgets = {
            "bill_no": forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super(IceBillForm, self).__init__(*args, **kwargs)
        self.fields.keyOrder = [
            "bill_no",
            "company_name",
            "company_address",
            "date"
        ]


class IceBillContentForm(forms.ModelForm):

    class Meta:
        model = IceBillContent
        exclude = ("ice_bill",)


class SearchForm(forms.Form):

    date = forms.DateField(initial=today, widget=forms.DateInput(format="%d/%m/%Y"), input_formats=("%d/%m/%Y",))
