# Generated by Django 4.1.3 on 2022-11-16 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_balancebikeuser'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BalanceBikeUser',
            new_name='Customer',
        ),
    ]