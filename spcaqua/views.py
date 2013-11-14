import os
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.core.context_processors import csrf
from django.forms.formsets import formset_factory, BaseFormSet
from spcaqua.forms import PurchaseBillForm, PurchaseBillContentForm, CompanyBillForm, CompanyBillContentForm



class RequiredFormSet(BaseFormSet):
    def __init__(self, *args, **kwargs):
        super(RequiredFormSet, self).__init__(*args, **kwargs)
        for form in self.forms:
            form.empty_permitted = False


def home(request):
    return render_to_response('home.html',
                              context_instance=RequestContext(request))

@login_required(login_url=reverse_lazy('login'))
def menu(request):
    return render_to_response('menu.html',
                              context_instance=RequestContext(request))
                              
@login_required(login_url=reverse_lazy('login'))
def search(request):
    return render_to_response('search.html',
                              context_instance=RequestContext(request))
                              
@login_required(login_url=reverse_lazy('login'))
def add_purchase_bill(request):

    PurchaseBillContentFormSet = formset_factory(PurchaseBillContentForm, max_num=5, extra=5, formset=RequiredFormSet)

    if request.method == 'POST':
        purchase_bill_form = PurchaseBillForm(request.POST)
        purchase_bill_content_formset = PurchaseBillContentFormSet(request.POST)

        if purchase_bill_content_formset.is_valid() and purchase_bill_form.is_valid():
            total_quantity = 0
            total_price = 0
            for form in purchase_bill_content_formset.forms:
                total_quantity += form.cleaned_data["quantity"]
                total_price += form.cleaned_data["price"]
            purchase_bill = purchase_bill_form.save(commit=False)
            purchase_bill.total_quantity = total_quantity
            purchase_bill.total_price = total_price
            purchase_bill.save()
            for form in purchase_bill_content_formset.forms:
                purchase_bill_content = form.save(commit=False)
                purchase_bill_content.purchase_bill = purchase_bill
                purchase_bill_content.save()
            return redirect("menu")
    else:
        purchase_bill_form = PurchaseBillForm()
        purchase_bill_content_formset = PurchaseBillContentFormSet()

    ctx = {"bill_form": purchase_bill_form,
           "bill_content_formset": purchase_bill_content_formset,
           "bill_type": "purchase",}
    ctx.update(csrf(request))

    return render_to_response('bill.html', ctx)
                              
@login_required(login_url=reverse_lazy('login'))
def add_company_bill(request):

    CompanyBillContentFormSet = formset_factory(CompanyBillContentForm, max_num=5, extra=5, formset=RequiredFormSet)

    if request.method == 'POST':
        company_bill_form = CompanyBillForm(request.POST)
        company_bill_content_formset = CompanyBillContentFormSet(request.POST)

        if company_bill_content_formset.is_valid() and company_bill_form.is_valid():
            total_quantity = 0
            total_price = 0
            for form in company_bill_content_formset.forms:
                total_quantity += form.cleaned_data["quantity"]
                total_price += form.cleaned_data["price"]
            company_bill = company_bill_form.save(commit=False)
            company_bill.total_quantity = company_quantity
            company_bill.total_price = company_price
            company_bill.save()
            for form in company_bill_content_formset.forms:
                company_bill_content = form.save(commit=False)
                company_bill_content.company_bill = company_bill
                company_bill_content.save()
            return redirect("menu")
    else:
        company_bill_form = CompanyBillForm()
        company_bill_content_formset = CompanyBillContentFormSet()

    ctx = {"bill_form": company_bill_form,
           "bill_content_formset": company_bill_content_formset,
           "bill_type": "company",}
    ctx.update(csrf(request))

    return render_to_response('bill.html', ctx)
                              
@login_required(login_url=reverse_lazy('login'))
def print_purchase_bill(request):
    return render_to_response('printbill.html',
                              context_instance=RequestContext(request))
                              
@login_required(login_url=reverse_lazy('login'))
def print_company_bill(request):
    return render_to_response('printbill.html',
                              context_instance=RequestContext(request))
