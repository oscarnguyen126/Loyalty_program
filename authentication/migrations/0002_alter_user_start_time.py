# Generated by Django 4.2.5 on 2023-09-20 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='start_time',
            field=models.DateField(auto_now=True),
        ),
    ]
