# Generated by Django 5.1.4 on 2025-01-03 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coderr_auth', '0009_alter_fileupload_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='uploads/'),
        ),
        migrations.AddField(
            model_name='profile',
            name='uploaded_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.DeleteModel(
            name='FileUpload',
        ),
    ]