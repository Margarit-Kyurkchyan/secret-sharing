# Generated by Django 4.2.7 on 2023-11-16 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Secret',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('secret_text', models.TextField()),
                ('unique_url', models.CharField(max_length=100, unique=True)),
                ('views_remaining', models.IntegerField(default=1)),
            ],
        ),
    ]
