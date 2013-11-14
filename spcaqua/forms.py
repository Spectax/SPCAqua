from django import forms

from spcaqua.models import CompanyBill, PurchaseBill, CompanyBillContent, PurchaseBillContent


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
