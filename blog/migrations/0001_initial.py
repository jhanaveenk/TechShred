# Generated by Django 4.1.5 on 2023-01-29 01:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Writer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_publish', models.DateField(auto_created=True)),
                ('title', models.CharField(max_length=100)),
                ('sub_heading', models.CharField(max_length=300)),
                ('content', models.TextField(max_length=5000)),
                ('writer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.writer')),
            ],
            options={
                'ordering': ['date_of_publish'],
            },
        ),
    ]
