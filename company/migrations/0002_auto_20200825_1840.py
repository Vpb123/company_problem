# Generated by Django 3.0.8 on 2020-08-25 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='problems',
            options={'ordering': ['problem']},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['Name']},
        ),
        migrations.RemoveField(
            model_name='student',
            name='problems',
        ),
        migrations.AddField(
            model_name='student',
            name='problems',
            field=models.ManyToManyField(to='company.Problems'),
        ),
    ]