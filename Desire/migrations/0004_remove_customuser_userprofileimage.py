# Generated by Django 4.2.1 on 2023-05-31 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Desire', '0003_rename_userimage_customuser_userprofileimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='userProfileImage',
        ),
    ]
