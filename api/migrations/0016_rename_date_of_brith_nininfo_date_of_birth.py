# Generated by Django 4.0.4 on 2022-07-02 19:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0015_alter_user_avatar"),
    ]

    operations = [
        migrations.RenameField(
            model_name="nininfo",
            old_name="date_of_birth",
            new_name="date_of_birth",
        ),
    ]
