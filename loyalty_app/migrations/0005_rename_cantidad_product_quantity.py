# Generated by Django 4.2.5 on 2023-09-21 00:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loyalty_app', '0004_remove_category_product_id_product_category_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='cantidad',
            new_name='quantity',
        ),
    ]
