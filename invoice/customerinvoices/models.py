from decimal import Decimal, ROUND_HALF_UP
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    brand_name = models.CharField(max_length=150, null=True)

    def __str__(self):
        return self.brand_name
    def get_absolute_url(self):
        return reverse("profile_detail", kwargs={"pk": self.pk})
    

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email_address = models.EmailField(max_length=254, null=True, blank=True)
    phone_number = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name



class Invoice(models.Model):
    CHOICES = (

    ('Unpaid', 'Unpaid'),
    ('Paid', 'Paid'),
)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer= models.ForeignKey(Customer, on_delete=models.CASCADE)
    description = models.CharField(max_length=225)
    discount_percentage = models.IntegerField(null=True, blank=True)
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices= CHOICES , default='UnPaid')

    def save(self, *args, **kwargs):
        if self.discount_percentage is not None and self.amount is not None:
            discount_factor = self.discount_percentage / 100
            discount = Decimal(self.amount) * Decimal(discount_factor)
            self.amount -= discount.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

        super().save(*args, **kwargs)  # Call the real save() method

    def __str__(self):
        return self.customer.name



class Receipt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer= models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='receipts')
    description = models.CharField(max_length=225)
    discount_percentage = models.IntegerField(null=True, blank=True)
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.discount_percentage is not None and self.amount is not None:
            discount_factor = self.discount_percentage / 100
            discount = Decimal(self.amount) * Decimal(discount_factor)
            self.amount -= discount.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

        super().save(*args, **kwargs)  # Call the real save() method

    def __str__(self):
        return self.customer.name    

