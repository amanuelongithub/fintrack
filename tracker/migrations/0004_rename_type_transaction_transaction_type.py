# Generated by Django 5.2.4 on 2025-07-24 00:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0003_rename_desc_transaction_detail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='type',
            new_name='transaction_type',
        ),
    ]
