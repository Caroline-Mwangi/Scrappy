# Generated by Django 4.1.7 on 2023-03-29 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search_tag', models.CharField(max_length=100)),
                ('tweet', models.CharField(max_length=10000)),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
