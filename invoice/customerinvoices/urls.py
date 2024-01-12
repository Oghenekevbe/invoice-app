from django.urls import path
from .views import (
    CustomerListView, CustomerDetailView, CustomerCreateView,
    CustomerUpdateView, CustomerDeleteView,
    InvoiceListView, InvoiceDetailView, InvoiceCreateView,
    InvoiceUpdateView, InvoiceDeleteView,
    ReceiptListView, ReceiptDetailView, ReceiptCreateView,
    ReceiptUpdateView, ReceiptDeleteView, ProfileDetailView, ProfileCreateView, ProfileUpdateView
)
from . import views


urlpatterns = [
    path('', views.Welcome, name='welcome'),
    path('detail_to_pdf/<str:model>/<int:pk>/', views.detail_to_pdf, name='detail_to_pdf'),

    # Customer URLs
    path('customers/', CustomerListView.as_view(), name='customer_list'),
    path('customers/<int:pk>/', CustomerDetailView.as_view(), name='customer_detail'),
    path('customers/create/', CustomerCreateView.as_view(), name='customer_create'),
    path('customers/<int:pk>/update/', CustomerUpdateView.as_view(), name='customer_update'),
    path('customers/<int:pk>/delete/', CustomerDeleteView.as_view(), name='customer_delete'),

    # Invoice URLs
    path('invoices/', InvoiceListView.as_view(), name='invoice_list'),
    path('invoices/<int:pk>/', InvoiceDetailView.as_view(), name='invoice_detail'),
    path('invoices/create/', InvoiceCreateView.as_view(), name='invoice_create'),
    path('invoices/<int:pk>/update/', InvoiceUpdateView.as_view(), name='invoice_update'),
    path('invoices/<int:pk>/delete/', InvoiceDeleteView.as_view(), name='invoice_delete'),

    # Receipt URLs
    path('receipts/', ReceiptListView.as_view(), name='receipt_list'),
    path('receipts/<int:pk>/', ReceiptDetailView.as_view(), name='receipt_detail'),
    path('receipts/create/', ReceiptCreateView.as_view(), name='receipt_create'),
    path('receipts/<int:pk>/update/', ReceiptUpdateView.as_view(), name='receipt_update'),
    path('receipts/<int:pk>/delete/', ReceiptDeleteView.as_view(), name='receipt_delete'),

    #profile ur;s   
    path('profiles/<int:pk>/', ProfileDetailView.as_view(), name='profile_detail'),
    path('profiles/create/', ProfileCreateView.as_view(), name='profile_create'),
    path('profiles/<int:pk>/update/', ProfileUpdateView.as_view(), name='profile_update'),

]
