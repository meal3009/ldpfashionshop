from rest_framework import serializers
from shop.models import Category,Product,Banner

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('url','id', 'name')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('url','id', 'code','name','category','sub_description','description','price','sale',
        'image_main','image_1','image_2','image_3','image_4','image_5','published','created','updated')

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = ('url','id', 'name','bannerimage1','urls1','bannerimage2','urls2','bannerimage3','urls3','bannerimage4','urls4','bannerimage5','urls5','bannerimage6','urls6')


