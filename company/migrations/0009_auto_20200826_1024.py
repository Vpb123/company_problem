# Generated by Django 3.0.8 on 2020-08-26 04:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0008_auto_20200826_0953'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='problems',
        ),
        migrations.AddField(
            model_name='student',
            name='problems',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='company.Problems'),
        ),
    ]
