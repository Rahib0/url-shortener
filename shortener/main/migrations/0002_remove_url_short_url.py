# Generated by Django 4.0.2 on 2022-02-02 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='url',
            name='short_url',
        ),
    ]
