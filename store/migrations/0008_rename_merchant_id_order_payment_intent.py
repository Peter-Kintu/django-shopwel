# Generated by Django 4.2.4 on 2023-09-24 23:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_orderitem_price_orderitem_quantity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='merchant_id',
            new_name='payment_intent',
        ),
    ]