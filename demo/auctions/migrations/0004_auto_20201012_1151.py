# Generated by Django 3.1 on 2020-10-12 08:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_auto_20201012_1147'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Watch_data',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='who_want_buy',
        ),
    ]
