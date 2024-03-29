# Generated by Django 4.0.5 on 2022-11-07 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('go_app', '0014_auto_20221010_2239'),
    ]

    operations = [
        migrations.RenameField(
            model_name='busdetails',
            old_name='user',
            new_name='bus_owner',
        ),
        migrations.RenameField(
            model_name='schedule',
            old_name='reaching_place',
            new_name='taken_from',
        ),
        migrations.RenameField(
            model_name='schedule',
            old_name='taking_place',
            new_name='to',
        ),
        migrations.AlterUniqueTogether(
            name='schedule',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='busdetails',
            name='contact',
        ),
        migrations.AddField(
            model_name='busdetails',
            name='bus_type',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='busdetails',
            name='running_way',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='busdetails',
            name='stopping_place',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='busdetails',
            name='stopping_time',
            field=models.TimeField(default='17:49:46'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='busdetails',
            name='taking_place',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='busdetails',
            name='taking_time',
            field=models.TimeField(default='17:49:46'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='account',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='busdetails',
            name='bus_no',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='busdetails',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='signup',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterModelTable(
            name='schedule',
            table=None,
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='bus',
        ),
    ]
