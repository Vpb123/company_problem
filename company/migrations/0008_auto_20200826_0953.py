# Generated by Django 3.0.8 on 2020-08-26 04:23

import company.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0007_auto_20200826_0949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problems',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='images/', validators=[company.models.validate_image, django.core.validators.FileExtensionValidator(allowed_extensions=['jpeg', 'jpg', 'pdf'])]),
        ),
        migrations.AlterField(
            model_name='sol_progress',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='images/', validators=[company.models.validate_image, django.core.validators.FileExtensionValidator(allowed_extensions=['jpeg', 'jpg', 'pdf'])]),
        ),
    ]
