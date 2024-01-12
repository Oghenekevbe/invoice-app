from typing import Any
from .forms import CustomerForm, InvoiceForm, ReceiptForm,ProfileForm
from .models import Customer, Invoice, Receipt, Profile
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpRequest, HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

import os
from django.conf import settings
from io import BytesIO
import urllib.request


def link_callback(uri, rel):
    # Convert image URIs to BytesIO objects
    if uri.startswith('http') or uri.startswith('https'):
        img_data = urllib.request.urlopen(uri).read()
        return BytesIO(img_data)

    # Handle local file references
    return os.path.join(settings.MEDIA_ROOT, uri.replace(settings.MEDIA_URL, ""))

def detail_to_pdf(request, model, pk):
    # Get the model dynamically (either Receipt or Invoice)
    model_class = Receipt if model == 'Receipt' else Invoice

    # Retrieve the object using the primary key
    obj = model_class.objects.get(pk=pk)
        # Retrieve the user associated with the current request
    user = request.user
    

    # Retrieve the profile for the user
    profile = get_object_or_404(Profile, user=user)

    # Render the HTML template with the object and model type
    template_path = 'pdf_template.html'  # Adjust to your template naming convention
    template = get_template(template_path)
    html = template.render({'object': obj, 'model': model, 'profile': profile})
    
    # Format parts of the filename to ensure they are safe
    customer_name = slugify(obj.customer.name)
    created_at = obj.created_at.strftime('%Y-%m-%d_%H-%M-%S')

    # Create a response with the content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'filename={customer_name}_{created_at}_{model}_detail_{pk}.pdf'

    # Create PDF from HTML content, using the link_callback function
    pisa_status = pisa.CreatePDF(html, dest=response, link_callback=link_callback)

    if pisa_status.err:
        return HttpResponse(f'We had some errors with code {pisa_status.err} <pre>{html}</pre>')

    return response




#welcomeview
def Welcome(request):
    return render(request, 'welcome.html')
 

# Customer views
class CustomerListView(LoginRequiredMixin,ListView):
    model = Customer
    template_name = 'customer_list.html'


class CustomerDetailView(LoginRequiredMixin,DetailView):
    model = Customer
    template_name = 'customer_detail.html'

class CustomerCreateView(LoginRequiredMixin,CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'customer_create.html'  
    success_url = reverse_lazy('customer_list')

    def form_valid(self, form):
        # Set the user field before saving the form
        form.instance.user = self.request.user
        return super().form_valid(form)

class CustomerUpdateView(LoginRequiredMixin,UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'customer_update.html'  
    success_url = reverse_lazy('customer_list')

    def form_valid(self, form):
        # Set the user field before saving the form
        form.instance.user = self.request.user
        return super().form_valid(form)

class CustomerDeleteView(LoginRequiredMixin,DeleteView):
    model = Customer
    template_name = 'customer_delete.html'  
    success_url = reverse_lazy('customer_list')


# Invoice views
class InvoiceListView(LoginRequiredMixin,ListView):
    model = Invoice
    template_name = 'invoice_list.html'

    

class InvoiceDetailView(LoginRequiredMixin,DetailView):
    model = Invoice
    template_name = 'invoice_detail.html'

class InvoiceCreateView(LoginRequiredMixin,CreateView):
    model = Invoice
    form_class = InvoiceForm
    template_name = 'invoice_create.html'  
    success_url = reverse_lazy('invoice_list')

    def form_valid(self, form):
        # Set the user field before saving the form
        form.instance.user = self.request.user
        return super().form_valid(form)

class InvoiceUpdateView(LoginRequiredMixin,UpdateView):
    model = Invoice
    form_class = InvoiceForm
    template_name = 'invoice_update.html'  
    success_url = reverse_lazy('invoice_list')

    def form_valid(self, form):
        # Set the user field before saving the form
        form.instance.user = self.request.user
        return super().form_valid(form)

class InvoiceDeleteView(LoginRequiredMixin,DeleteView):
    model = Invoice
    template_name = 'invoice_delete.html'  
    success_url = reverse_lazy('invoice_list')

# Receipt views
class ReceiptListView(LoginRequiredMixin,ListView):
    model = Receipt
    template_name = 'receipt_list.html'

class ReceiptDetailView(LoginRequiredMixin,DetailView):
    model = Receipt
    template_name = 'receipt_detail.html'

class ReceiptCreateView(LoginRequiredMixin,CreateView):
    model = Receipt
    form_class = ReceiptForm
    template_name = 'receipt_create.html'  
    success_url = reverse_lazy('receipt_list')

    def form_valid(self, form):
        # Set the user field before saving the form
        form.instance.user = self.request.user
        return super().form_valid(form)

class ReceiptUpdateView(LoginRequiredMixin,UpdateView):
    model = Receipt
    form_class = ReceiptForm
    template_name = 'receipt_update.html'  
    success_url = reverse_lazy('receipt_list')

    def form_valid(self, form):
        # Set the user field before saving the form
        form.instance.user = self.request.user
        return super().form_valid(form)

class ReceiptDeleteView(LoginRequiredMixin,DeleteView):
    model = Receipt
    template_name = 'receipt_delete.html'  
    success_url = reverse_lazy('receipt_list')






class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profile_detail.html'

class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'profile_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    

class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'profile_form.html'
    success_url = reverse_lazy('welcome')

