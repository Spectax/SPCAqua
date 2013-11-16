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

    class Meta:
        model = CompanyBill
        exclude = ("total_price", "total_quantity",)
        widgets = {
            "bill_no": forms.HiddenInput(),
            "date": forms.HiddenInput(),
        }


class CompanyBillContentForm(forms.ModelForm):

    class Meta:
        model = CompanyBillContent
        exclude = ("company_bill",)


class PurchaseBillForm(forms.ModelForm):

    class Meta:
        model = PurchaseBill
        exclude = ("total_price", "total_quantity",)
        widgets = {
            "bill_no": forms.HiddenInput(),
            "date": forms.HiddenInput(),
        }


class PurchaseBillContentForm(forms.ModelForm):

    class Meta:
        model = PurchaseBillContent
        exclude = ("purchase_bill",)


class LotForm(forms.ModelForm):

    class Meta:
        model = Lot
        exclude= ("total_quantity",)
        widgets = {
            "lot_no": forms.HiddenInput(),
            "date": forms.HiddenInput(),
        }


class LotContentForm(forms.ModelForm):

    class Meta:
        model = LotContent
        exclude = ("lot",)


class IceBillForm(forms.ModelForm):

    class Meta:
        model = IceBill
        widgets = {
            "bill_no": forms.HiddenInput(),
            "date": forms.HiddenInput(),
        }


class IceBillContentForm(forms.ModelForm):

    class Meta:
        model = IceBillContent
        exclude = ("ice_bill",)


class SearchForm(forms.Form):

    date = forms.DateField(initial=today, widget=forms.DateInput(format="%d/%m/%Y"), input_formats=("%d/%m/%Y",))
