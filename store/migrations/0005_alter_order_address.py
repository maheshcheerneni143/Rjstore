# Generated by Django 4.1.7 on 2023-03-20 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_order_orderitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(max_length=150),
        ),
    ]
