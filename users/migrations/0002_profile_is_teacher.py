# Generated by Django 3.0.3 on 2020-03-01 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_teacher',
            field=models.BooleanField(default=False, verbose_name='teacher status'),
        ),
    ]