from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save, post_save
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.signals import user_logged_in
from django.utils.text import slugify
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
from allauth.account.signals import email_confirmed
import stripe
from django.utils import timezone

# stripe.api_key = settings.STRIPE_SECRET_KEY

User = get_user_model()



class AutoDateTimeField(models.DateTimeField):
    def pre_save(self, model_instance, add):
        return timezone.now()


class Pricing(models.Model):
    name = models.CharField(max_length=100)  # Basic / Pro / Premium
    slug = models.SlugField()
    stripe_price_id = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    currency = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Subscription(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    pricing = models.ForeignKey(Pricing, on_delete=models.CASCADE, related_name='subscriptions')
    created = models.DateTimeField(auto_now_add=True)
    stripe_subscription_id = models.CharField(max_length=50)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.user.email

#     @property
#     def is_active(self):
#         return self.status == "active" or self.status == "trialing"


class Course(models.Model):
    pricing_tiers = models.ManyToManyField(Pricing, blank=True)
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    thumbnail = models.ImageField(upload_to="thumbnails/", default='default_img_for_not_pro_user/default_img_for_not_pro_user.jpg')
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("content:course-detail", kwargs={"slug": self.slug})



class Order(models.Model):
    user = models.ForeignKey(
        User, blank=True, null=True, on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    ordered_date = models.DateTimeField(blank=True, null=True)
    ordered = models.BooleanField(default=False, null=True, blank=True)
    
   
    def __str__(self):
        return self.reference_number

    @property
    def reference_number(self):
        return f"ORDER-{self.pk}"



class Store(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateField(default=timezone.now)
    updated_at = AutoDateTimeField(default=timezone.now)    
        
    def __str__(self):
        return self.name
        

class Video(models.Model):

    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )


    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='videos')
    vimeo_id = models.CharField(max_length=50)
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    # description = models.TextField()
    order = models.IntegerField(default=1)



    # name_of_product = models.CharField(max_length=100)
    # slug = models.SlugField(unique=True)
    shopify_links = models.CharField(blank=True, null=True, max_length=500, help_text = "A link that will take to a single the store")
    name_of_store = models.ForeignKey(Store, related_name='store_name', blank=True, null=True, on_delete=models.PROTECT)
    # categories = models.ForeignKey(Category, blank=True, null=True, on_delete=models.CASCADE)
    # otherShopifyLinks = models.ForeignKey(OtherShopifyLinks, related_name='other_shopify_links',  blank=True, null=True, on_delete=models.PROTECT)
    # OtherAliexpressSuppliersLinks = models.ForeignKey(OtherAliexpressSuppliersLinks, related_name='OtherAliexpressSuppliersLinks',  blank=True, null=True, on_delete=models.PROTECT)
    # technologies = models.ForeignKey(Technology, related_name='technologies', blank=True, null=True, on_delete=models.PROTECT)
    shopify_price = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=2, help_text = "Product price from shopify")
    product_thumbnail = models.ImageField(blank=True, null=True, upload_to="thumbnails/", default='products/defaut_image_store_light_blue_bag.jpg')
    store_logo = models.ImageField(blank=True, null=True, upload_to="image_store/",default='products/defaut_image_store.png')
    aliexpress_order = models.IntegerField(default=0, help_text = "Amount of aliexpress order generated")
    aliexpress_price = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=2, help_text = "Product price from aliexpress")
    facebook_shares = models.IntegerField(blank=True, null=True, default=0, help_text = "Amount of shares generated")
    facebook_comment = models.IntegerField(default=0, help_text = "Amount of comment generated")
    facebook_views = models.IntegerField(default=0, help_text = "Amount of views generated")
    facebook_like = models.IntegerField(default=0, help_text = "Amount of facebook like")
    facebook_wow = models.IntegerField(default=0, help_text = "Amount of facebook wow")
    facebook_love = models.IntegerField(default=0, help_text = "Amount of facebook love")
    facebook_haha = models.IntegerField(default=0, help_text = "Amount of facebook haha")
    facebook_sad = models.IntegerField(default=0, help_text = "Amount of facebook sad")
    facebook_angry = models.IntegerField(default=0, help_text = "Amount of facebook angry")
    # links_to_ads = RichTextUploadingField(blank=True, null=True,  help_text = "A link that will take to ads")
    # links_to_others_stores = RichTextUploadingField(blank=True, null=True,help_text = "A link that will take to the store", )
    # links_to_others_suppliers = RichTextUploadingField(blank=True, null=True,)
    text_that_comes_with_ads = RichTextUploadingField(blank=True, null=True)
    read_more_text_that_comes_with_ads = RichTextUploadingField(blank=True, null=True)
    number_of_store_selling = models.IntegerField(default=0, help_text = "Amount of store selling the product")
    number_of_suppliers_selling= models.IntegerField( default=0, help_text = "Amount of suppliers selling the product")
    created_at = models.DateField(default=timezone.now)
    # languages = models.ForeignKey(Language,  related_name='languages', blank=True, null=True, on_delete=models.PROTECT)
    # buttons = models.ForeignKey(Button, related_name='buttons', blank=True, null=True, on_delete=models.PROTECT)
    # countries = models.ForeignKey(Country, blank=True, null=True, on_delete=models.PROTECT)
    
    is_faceBook = models.BooleanField(default=False)
    is_pinterest = models.BooleanField(default=False)
    is_tiktok = models.BooleanField(default=False)
    has_video = models.BooleanField(default=False)
    has_photo = models.BooleanField(default=False)
    price_margin = models.DecimalField(default=0, max_digits=10, decimal_places=2, help_text = "Profit you get from this product")
    updated_at = AutoDateTimeField(default=timezone.now)
    aliexpress_total_sale = models.DecimalField(default=0, max_digits=10, decimal_places=2, help_text = "Amount of aliexpress sale generated")



    # def get_absolute_url(self):
    #     return reverse("product:product-detail", kwargs={"slug": self.slug})

    
    # def save(self, *args, **kwargs):
    #     for lang_code, lang_verbose in settings.LANGUAGES:
    #         if hasattr(self, 'slug_%s' % lang_code) and hasattr(self, 'name_of_product_%s' % lang_code):
    #             setattr(self, 'slug_%s' % lang_code, slugify(getattr(self, 'name_of_product_%s' % lang_code, u"")))
    #     super(Product, self).save(*args, **kwargs)


    def get_absolute_url(self):
        return reverse("content:course-detail", kwargs={"slug": self.slug})
    
    def get_update_url(self):
        return reverse("staff:product-update", kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse("staff:product-delete", kwargs={'pk': self.pk})


    @property
    def imageURL(self):
        try:
            url = self.image_store.url
        except:
            url = ''
        print('URL:', url)
        return url

    def __str__(self):
        return f'{self.name_of_product} (${self.aliexpress_price})' 
    

    def save(self, *args, **kwargs):
         
        self.price_margin = self.shopify_price - self.aliexpress_price 

        self.aliexpress_total_sale = self.aliexpress_order * self.shopify_price

        super().save(*args, **kwargs)

    def img_preview(self): #new
        return mark_safe(f'<img src = "{self.product_thumbnail.url}" width = "50"/>')
        
    img_preview.short_description = 'Product Image'
    img_preview.allow_tags = True

    class Meta:
        ordering = ["order"]    

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("content:video-detail", kwargs={
            "video_slug": self.slug,
            "slug": self.course.slug
        })


def pre_save_course(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.name)


def pre_save_video(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)


def post_email_confirmed(request, email_address, *args, **kwargs):
    user = User.objects.get(email=email_address.email)
    free_trial_pricing = Pricing.objects.get(name='Free Trial')
    subscription = Subscription.objects.create(
        user=user, 
        pricing=free_trial_pricing
    )
    # stripe_customer = stripe.Customer.create(
    #     email=user.email
    # )
    # stripe_subscription = stripe.Subscription.create(
    #     customer=stripe_customer["id"],
    #     items=[{'price': 'django-free-trial'}],
    #     trial_period_days=7
    # )
    # subscription.status = stripe_subscription["status"]  # trialing
    # subscription.stripe_subscription_id = stripe_subscription["id"]
    # subscription.save()
    # user.stripe_customer_id = stripe_customer["id"]
    user.save()


# def user_logged_in_receiver(sender, user, **kwargs):
#     subscription = user.subscription
#     sub = stripe.Subscription.retrieve(subscription.stripe_subscription_id)

#     subscription.status = sub["status"]
#     subscription.save()


# user_logged_in.connect(user_logged_in_receiver)
email_confirmed.connect(post_email_confirmed)
pre_save.connect(pre_save_course, sender=Course)
pre_save.connect(pre_save_video, sender=Video)