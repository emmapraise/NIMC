# Generated by Django 4.0.4 on 2022-07-11 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0022_cv'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='access_code',
            field=models.CharField(default='1234', max_length=6),
        ),
    ]
