# Generated by Django 3.0.6 on 2020-05-26 18:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('superapp', '0004_customer_orders'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='orders',
        ),
        migrations.AddField(
            model_name='customer',
            name='orders',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='superapp.Product'),
        ),
    ]
