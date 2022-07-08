# Generated by Django 4.0.4 on 2022-07-07 04:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_remove_educationdocument_document_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='educationdocument',
            name='name_of_school',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='educationdocument',
            name='certificate',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='education_certificate', to='api.document'),
        ),
        migrations.AlterField(
            model_name='educationdocument',
            name='transcript',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='education_transcript', to='api.document'),
        ),
        migrations.CreateModel(
            name='CertificateDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_at', models.DateTimeField(auto_now=True, null=True)),
                ('certificate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='certificate', to='api.document')),
                ('transcript', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transcript', to='api.document')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
