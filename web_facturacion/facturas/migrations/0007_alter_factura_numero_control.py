# Generated by Django 5.1.2 on 2024-11-08 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturas', '0006_alter_factura_forma_pago'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factura',
            name='numero_factura',
            field=models.CharField(max_length=20),
        ),
    ]
