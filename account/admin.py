from django.contrib import admin
from .models import Profile,Categoty,Product,Slide

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','location')
    list_display = ('user','birth_date','email_confirmed', 'location')
    list_filter = [ 'location', 'user' ]
    search_fields = ['location', 'user' ]


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','disprice','seller')
    list_display = ('name','disprice','seller', 'acprice','categoty')
    list_display_links = ('name','disprice','seller', 'acprice','categoty')
    list_filter = ['pub_date','categoty','seller']
    search_fields = ['categoty','seller','name']



class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','pub_date')
    list_display_links = ('name','pub_date')
    list_filter = ['pub_date','name']
    search_fields = ['id','name','pub_date']


class SlideAdmin(admin.ModelAdmin):
    list_display = ('image','pub_date')
    list_display_links = ('image','pub_date')
    list_filter = ['pub_date','image']




admin.site.register(Profile,ProfileAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Categoty,CategoryAdmin)
admin.site.register(Slide,SlideAdmin)