# Generated by Django 4.0.5 on 2022-06-06 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_portal_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='time',
            new_name='creating_date_time',
        ),
        migrations.AddField(
            model_name='author',
            name='rating',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='comment',
            name='rating',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]