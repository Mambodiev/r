# Generated by Django 4.2 on 2023-06-07 12:15

import ckeditor_uploader.fields
import content.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0011_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='aliexpress_order',
            field=models.IntegerField(default=0, help_text='Amount of aliexpress order generated'),
        ),
        migrations.AddField(
            model_name='video',
            name='aliexpress_price',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Product price from aliexpress', max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='video',
            name='aliexpress_total_sale',
            field=models.DecimalField(decimal_places=2, default=0, help_text='Amount of aliexpress sale generated', max_digits=10),
        ),
        migrations.AddField(
            model_name='video',
            name='created_at',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='video',
            name='facebook_angry',
            field=models.IntegerField(default=0, help_text='Amount of facebook angry'),
        ),
        migrations.AddField(
            model_name='video',
            name='facebook_comment',
            field=models.IntegerField(default=0, help_text='Amount of comment generated'),
        ),
        migrations.AddField(
            model_name='video',
            name='facebook_haha',
            field=models.IntegerField(default=0, help_text='Amount of facebook haha'),
        ),
        migrations.AddField(
            model_name='video',
            name='facebook_like',
            field=models.IntegerField(default=0, help_text='Amount of facebook like'),
        ),
        migrations.AddField(
            model_name='video',
            name='facebook_love',
            field=models.IntegerField(default=0, help_text='Amount of facebook love'),
        ),
        migrations.AddField(
            model_name='video',
            name='facebook_sad',
            field=models.IntegerField(default=0, help_text='Amount of facebook sad'),
        ),
        migrations.AddField(
            model_name='video',
            name='facebook_shares',
            field=models.IntegerField(blank=True, default=0, help_text='Amount of shares generated', null=True),
        ),
        migrations.AddField(
            model_name='video',
            name='facebook_views',
            field=models.IntegerField(default=0, help_text='Amount of views generated'),
        ),
        migrations.AddField(
            model_name='video',
            name='facebook_wow',
            field=models.IntegerField(default=0, help_text='Amount of facebook wow'),
        ),
        migrations.AddField(
            model_name='video',
            name='has_photo',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='video',
            name='has_video',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='video',
            name='is_faceBook',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='video',
            name='is_pinterest',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='video',
            name='is_tiktok',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='video',
            name='number_of_store_selling',
            field=models.IntegerField(default=0, help_text='Amount of store selling the product'),
        ),
        migrations.AddField(
            model_name='video',
            name='number_of_suppliers_selling',
            field=models.IntegerField(default=0, help_text='Amount of suppliers selling the product'),
        ),
        migrations.AddField(
            model_name='video',
            name='price_margin',
            field=models.DecimalField(decimal_places=2, default=0, help_text='Profit you get from this product', max_digits=10),
        ),
        migrations.AddField(
            model_name='video',
            name='product_thumbnail',
            field=models.ImageField(blank=True, default='products/defaut_image_store_light_blue_bag.jpg', null=True, upload_to='thumbnails/'),
        ),
        migrations.AddField(
            model_name='video',
            name='shopify_links',
            field=models.CharField(blank=True, help_text='A link that will take to a single the store', max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='video',
            name='shopify_price',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Product price from shopify', max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='video',
            name='store_logo',
            field=models.ImageField(blank=True, default='products/defaut_image_store.png', null=True, upload_to='image_store/'),
        ),
        migrations.AddField(
            model_name='video',
            name='text_that_comes_with_ads',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='video',
            name='updated_at',
            field=content.models.AutoDateTimeField(default=django.utils.timezone.now),
        ),
    ]
