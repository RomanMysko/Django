# Generated by Django 3.1.3 on 2021-05-05 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0004_prices'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Prices',
            new_name='Price',
        ),
    ]