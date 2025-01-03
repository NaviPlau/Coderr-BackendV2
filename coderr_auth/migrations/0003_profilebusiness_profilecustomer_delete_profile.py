# Generated by Django 5.1.4 on 2025-01-02 19:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coderr_auth', '0002_profile_uploaded_at_alter_profile_description_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileBusiness',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, null=True, upload_to='uploads')),
                ('location', models.CharField(blank=True, default='Berlin', max_length=255, null=True)),
                ('tel', models.CharField(blank=True, default='12345678', max_length=20, null=True)),
                ('description', models.TextField(blank=True, default='Bitte Beschreibung hinzufügen', max_length=5000, null=True)),
                ('working_hours', models.CharField(blank=True, default='8-18', max_length=50, null=True)),
                ('type', models.CharField(default='business', max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='business_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProfileCustomer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, null=True, upload_to='uploads')),
                ('uploaded_at', models.DateTimeField(auto_now=True)),
                ('type', models.CharField(default='customer', max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='customer_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]