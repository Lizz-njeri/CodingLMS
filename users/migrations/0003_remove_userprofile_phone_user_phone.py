# Generated by Django 4.2.7 on 2023-11-23 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_user_phone_alter_userprofile_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='phone',
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
