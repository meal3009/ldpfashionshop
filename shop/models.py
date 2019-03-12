from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Product(models.Model):
    code = models.CharField(max_length=10,unique=True)
    name = models.CharField(max_length=100,unique=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    sub_description = models.CharField(max_length=200)
    description = models.TextField()
    price = models.PositiveIntegerField(verbose_name='price (฿)')
    image_main = models.ImageField(upload_to='products/products_main/%Y/%m/%d')
    image_1 = models.ImageField(upload_to='products/products/%Y/%m/%d',blank=True)
    image_2 = models.ImageField(upload_to='products/products/%Y/%m/%d',blank=True)
    image_3 = models.ImageField(upload_to='products/products/%Y/%m/%d',blank=True)
    image_4 = models.ImageField(upload_to='products/products/%Y/%m/%d',blank=True)
    image_5 = models.ImageField(upload_to='products/products/%Y/%m/%d',blank=True)
    published = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    sale = models.PositiveIntegerField(verbose_name='price_sale (฿)')

    def __str__(self):
        return self.name
    
class Banner(models.Model):
    name = models.CharField(max_length=200)
    bannerimage1 = models.ImageField(upload_to='products/banner/%Y/%m/%d')
    urls1 = models.URLField()
    bannerimage2 = models.ImageField(upload_to='products/banner/%Y/%m/%d')
    urls2 = models.URLField()
    bannerimage3 = models.ImageField(upload_to='products/banner/%Y/%m/%d')
    urls3 = models.URLField()
    bannerimage4 = models.ImageField(upload_to='products/banner/%Y/%m/%d')
    urls4 = models.URLField()
    bannerimage5 = models.ImageField(upload_to='products/banner/%Y/%m/%d')
    urls5 = models.URLField()
    bannerimage6 = models.ImageField(upload_to='products/banner/%Y/%m/%d')
    urls6 = models.URLField()

    def __str__(self):
        return self.name