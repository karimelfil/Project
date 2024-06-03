# Generated by Django 5.0.6 on 2024-05-28 08:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('returnpack', '0008_rename_item_id_payment_item_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bill',
            name='payement_terms',
        ),
        migrations.AddField(
            model_name='bill',
            name='payment_terms',
            field=models.CharField(choices=[('paid', 'Paid'), ('unpaid', 'Unpaid')], default='unpaid', max_length=20),
        ),
        migrations.AlterField(
            model_name='bill',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='returnpack.client'),
        ),
        migrations.AlterField(
            model_name='bill',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='bill',
            name='date_due',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='bill',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]