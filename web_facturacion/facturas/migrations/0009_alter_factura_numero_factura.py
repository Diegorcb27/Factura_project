# Generated by Django 5.1.2 on 2024-11-09 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturas', '0008_alter_factura_numero_factura'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factura',
            name='numero_factura',
            field=models.CharField(max_length=20),
        ),
    ]
