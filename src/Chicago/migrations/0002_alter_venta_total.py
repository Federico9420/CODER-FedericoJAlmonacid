# Generated by Django 5.1.4 on 2025-01-07 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Chicago', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='total',
            field=models.DecimalField(decimal_places=2, editable=False, max_digits=10),
        ),
    ]