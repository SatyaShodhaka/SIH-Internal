# Generated by Django 3.0.2 on 2020-01-25 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_userprofile_is_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='contact1',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='contact2',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='contact3',
            field=models.CharField(default='', max_length=10),
        ),
    ]