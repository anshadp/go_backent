# Generated by Django 4.0.5 on 2022-09-03 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('go_app', '0011_rename_username_account_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='user_type',
            field=models.CharField(max_length=100),
        ),
    ]
