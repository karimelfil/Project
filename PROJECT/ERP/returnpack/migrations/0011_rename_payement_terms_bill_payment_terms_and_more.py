# Generated by Django 5.0.6 on 2024-05-28 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('returnpack', '0010_remove_bill_payment_terms_bill_payement_terms_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bill',
            old_name='payement_terms',
            new_name='payment_terms',
        ),
        migrations.AlterField(
            model_name='bill',
            name='date',
            field=models.DateField(default='default value'),
        ),
        migrations.AlterField(
            model_name='bill',
            name='date_due',
            field=models.DateField(default='default value'),
        ),
    ]
