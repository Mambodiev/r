# Generated by Django 3.0.9 on 2020-08-25 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0007_auto_20200825_2121'),
    ]

    operations = [
        migrations.AddField(
            model_name='pricing',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
    ]
