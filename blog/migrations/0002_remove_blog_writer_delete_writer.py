# Generated by Django 4.1.5 on 2023-01-29 01:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='writer',
        ),
        migrations.DeleteModel(
            name='Writer',
        ),
    ]