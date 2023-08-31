# Generated by Django 4.2.4 on 2023-08-31 05:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='followings',
            field=models.ManyToManyField(related_name='follwers', to=settings.AUTH_USER_MODEL),
        ),
    ]
