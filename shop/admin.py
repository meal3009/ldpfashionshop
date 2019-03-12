from django.contrib import admin
from .models import Category, Product, Banner
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name']
admin.site.register(Category,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    search_fields = ['code','name','price']
    list_display = ['id','code', 'name', 'category','published','price','sale', 'updated']
    list_filter = ['created', 'updated']
    list_editable = ['published', 'price','sale']
    list_display_links = ['id','code', 'name']
    list_per_page = 20
admin.site.register(Product, ProductAdmin)

class BannerAdmin(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(Banner,BannerAdmin)