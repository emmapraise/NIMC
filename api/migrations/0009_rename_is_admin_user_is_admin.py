# Generated by Django 4.0.4 on 2022-05-21 23:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_user_is_citizen'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_Admin',
            new_name='is_admin',
        ),
    ]
