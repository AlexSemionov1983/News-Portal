# Generated by Django 4.0.5 on 2022-06-07 22:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news_portal_app', '0002_rename_time_post_creating_date_time_author_rating_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]