from django import forms

from spcaqua.models import CompanyBill, PurchaseBill, CompanyBillContent, PurchaseBillContent


class CompanyBillForm(forms.ModelForm):

    class Meta:
        model = CompanyBill
        widgets = {
            "bill_no": forms.HiddenInput(),
        }


class CompanyBillContentForm(forms.ModelForm):

    class Meta:
        model = CompanyBillContent
        exclude = ("company_bill",)


class PurchaseBillForm(forms.ModelForm):

    class Meta:
        model = PurchaseBill
        widgets = {
            "bill_no": forms.HiddenInput(),
        }


class PurchaseBillContentFrom(forms.ModelForm):

    class Meta:
        model = PurchaseBillContent
        exclude = ("purchase_bill",)
