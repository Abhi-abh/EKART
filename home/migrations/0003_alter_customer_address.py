# Generated by Django 5.1.1 on 2024-10-26 15:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0002_product_delete_status_product_priority_customer_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customer",
            name="address",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
