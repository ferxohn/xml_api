# Generated by Django 3.2.9 on 2021-11-19 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_cfdi_cfdiissued_cfdireceived'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cfdi',
            name='subtotal',
            field=models.DecimalField(decimal_places=2, max_digits=13),
        ),
        migrations.AlterField(
            model_name='cfdi',
            name='total',
            field=models.DecimalField(decimal_places=2, max_digits=13),
        ),
    ]