# Generated by Django 4.0.4 on 2022-08-17 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0026_remove_request_status_updatenininfo_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='updatenininfo',
            name='document',
            field=models.FileField(blank=True, null=True, upload_to='NIMC/static/documents'),
        ),
    ]
