import os
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy

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
    return render_to_response('bill.html',
                              context_instance=RequestContext(request))
                              
@login_required(login_url=reverse_lazy('login'))
def add_company_bill(request):
    return render_to_response('bill.html',
                              context_instance=RequestContext(request))
                              
@login_required(login_url=reverse_lazy('login'))
def print_purchase_bill(request):
    return render_to_response('printbill.html',
                              context_instance=RequestContext(request))
                              
@login_required(login_url=reverse_lazy('login'))
def print_company_bill(request):
    return render_to_response('printbill.html',
                              context_instance=RequestContext(request))
