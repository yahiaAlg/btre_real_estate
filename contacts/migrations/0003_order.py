# Generated by Django 5.0.4 on 2024-04-05 18:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_alter_contact_id'),
        ('listings', '0002_alter_listing_id'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
                ('discount', models.DecimalField(decimal_places=2, max_digits=5)),
                ('status', models.CharField(choices=[('IN_STOREHOUSE', 'In Storehouse'), ('SHIPPED', 'Shipped'), ('ARRIVED', 'Arrived')], default='IN_STOREHOUSE', max_length=13)),
                ('purchase_date', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('listing', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='listings.listing')),
            ],
        ),
    ]
