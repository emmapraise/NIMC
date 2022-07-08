# Generated by Django 4.0.4 on 2022-07-04 00:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_merge_0016_alter_user_email_0017_user_middle_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='path',
            field=models.FileField(upload_to='NIMC/static/documents'),
        ),
        migrations.AlterField(
            model_name='document',
            name='type',
            field=models.CharField(choices=[('Old National ID Card', 'Old National ID Card'), ('Driver’s License', 'Driver’s License'), ('Voter’s card (Temporary or Permanent)', 'Voter’s card (Temporary or Permanent)'), ('Nigerian International passport', 'Nigerian International passport'), ('Certificate of Origin', 'Certificate of Origin'), ('Curriculum Vitae', 'Curriculum Vitae'), ('Certificate', 'Certificate'), ('Transcript', 'Transcript')], max_length=100),
        ),
        migrations.AlterField(
            model_name='nininfo',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='NIMC/static/images'),
        ),
        migrations.CreateModel(
            name='ProfessionalDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_at', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=100)),
                ('year_of_achievement', models.CharField(max_length=4)),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.document')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EducationDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_at', models.DateTimeField(auto_now=True, null=True)),
                ('highest_education', models.CharField(choices=[('Primary Education', 'Primary Education'), ('Secondary Education', 'Secondary Education'), ('Ordinary National Diploma', 'Ordinary National Diploma'), ('Higher National Diploma', 'Higher National Diploma'), ('Degree', 'Degree'), ('Masters', 'Masters'), ('Doctor of Philosophy', 'Doctor of Philosophy')], max_length=100)),
                ('year_of_graduation', models.CharField(max_length=4)),
                ('class_of_graduation', models.CharField(choices=[('First class', 'First Class'), ('Second class upper', 'Second Class Upper'), ('Second class lower', 'Second Class Lower'), ('Third class', 'Third Class'), ('Pass', 'Pass')], max_length=20)),
                ('country_of_graduation', models.CharField(max_length=20)),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.document')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
