# Generated by Django 4.2 on 2023-06-11 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0013_video_read_more_text_that_comes_with_ads'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='description',
        ),
    ]
