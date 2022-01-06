# Generated by Django 3.2.10 on 2021-12-25 23:49

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, default='Anonymous', max_length=14, verbose_name='Name')),
                ('body', models.CharField(blank=True, db_index=True, max_length=40, null=True, verbose_name='Body')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created DateTime')),
                ('likes', models.PositiveIntegerField(blank=True, db_index=True, default=0, verbose_name='like')),
                ('image', cloudinary.models.CloudinaryField(blank=True, db_index=True, max_length=255, verbose_name='image')),
            ],
            options={
                'db_table': 'post',
            },
        ),
    ]
