# Generated by Django 5.1.2 on 2024-11-01 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturas', '0004_alter_factura_cliente_delete_cliente'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='factura',
            name='usuario',
        ),
        migrations.AlterField(
            model_name='factura',
            name='rif',
            field=models.CharField(default='J-', max_length=12, unique=True),
        ),
    ]