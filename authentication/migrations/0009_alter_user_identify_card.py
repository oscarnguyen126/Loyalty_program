# Generated by Django 4.2.5 on 2023-09-26 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0008_alter_user_mobile_alter_user_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='identify_card',
            field=models.CharField(),
        ),
    ]