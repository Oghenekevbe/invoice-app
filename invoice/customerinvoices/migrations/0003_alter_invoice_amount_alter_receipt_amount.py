# Generated by Django 4.2.7 on 2023-11-26 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("customerinvoices", "0002_alter_customer_email_address_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="invoice",
            name="amount",
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
        migrations.AlterField(
            model_name="receipt",
            name="amount",
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
    ]
