# Generated by Django 2.2.3 on 2019-07-25 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0013_movie_like_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='like_count',
            field=models.IntegerField(default=0),
        ),
    ]
