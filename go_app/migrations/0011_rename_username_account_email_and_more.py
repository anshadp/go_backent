# Generated by Django 4.0.5 on 2022-08-14 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('go_app', '0010_rename_user_id_account_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='username',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='signup',
            old_name='email',
            new_name='username',
        ),
    ]
