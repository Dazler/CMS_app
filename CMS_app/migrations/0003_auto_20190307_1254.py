# Generated by Django 2.0.13 on 2019-03-07 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CMS_app', '0002_auto_20190307_1028'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsFeed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Airport', models.TextField(default='Heaven')),
                ('Content', models.TextField(default='Heaven')),
            ],
        ),
        migrations.AddField(
            model_name='aircraft',
            name='Flight_type',
            field=models.TextField(default='Based_on_button'),
        ),
    ]
