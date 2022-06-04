from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Category1(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'categories1'

    def get_absolute_url(self):
        return reverse('store:category_list', args=[self.slug])

    def __str__(self):
        return self.name


class Category2(models.Model):
    category = models.ForeignKey(Category1, related_name='brand', on_delete=models.CASCADE)
    brand_name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'categories2'

    def __str__(self):
        return self.brand_name
    
    
class Category3(models.Model):
    brand_name = models.ForeignKey(Category2, related_name='algorith', on_delete=models.CASCADE)
    algorith_or_models = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'categories3'

    def __str__(self):
        return self.algorith_or_models


class Product(models.Model):
    category1 = models.ForeignKey(Category1, related_name='product', on_delete=models.CASCADE)
    category2 = models.ForeignKey(Category2, related_name='product', on_delete=models.CASCADE)
    category3 = models.ForeignKey(Category3, related_name='product', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_creator')
    title = models.CharField(max_length=245)
    description = models.TextField(blank=True)
    image_1 = models.ImageField(upload_to='images/', blank=True, null=True)
    image_2 = models.ImageField(upload_to='images/', blank=True, null=True)
    image_3 = models.ImageField(upload_to='images/', blank=True, null=True)
    image_4 = models.ImageField(upload_to='images/', blank=True, null=True)
    image_5 = models.ImageField(upload_to='images/', blank=True, null=True)
    image_6 = models.ImageField(upload_to='images/', blank=True, null=True)
    image_7 = models.ImageField(upload_to='images/', blank=True, null=True)
    image_8 = models.ImageField(upload_to='images/', blank=True, null=True)
    image_9 = models.ImageField(upload_to='images/', blank=True, null=True)
    image_10 = models.ImageField(upload_to='images/', blank=True, null=True)
    slug = models.SlugField(max_length=245)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    count = models.IntegerField(default=1)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created',)

    def get_absolute_url(self):
        return reverse('store:product_detail', args=[self.slug])

    def __str__(self):
        return self.title
