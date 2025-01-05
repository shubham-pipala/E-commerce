from django.contrib import admin
from .models import *

# Register your models here.

class Blog_(admin.ModelAdmin):
    list_display = ['id','name','email']
    list_filter = ['id','name','email']

admin.site.register(Blog1,Blog_)

admin.site.register(Author) 

class Cat_(admin.ModelAdmin):
    list_display = ['id','name','image']
    list_filter = ['id','name','image']

admin.site.register(Category,Cat_)

class reg_(admin.ModelAdmin):
    list_display = ['id','name','email','mob','add','password']

admin.site.register(registeration,reg_)


class pro_(admin.ModelAdmin):
    list_display = ['id','name','price','category','stock']

admin.site.register(product,pro_)


class cart_(admin.ModelAdmin):
    list_display = ['id','userid','proid','orderid','qty']

admin.site.register(cart,cart_)

class ven_(admin.ModelAdmin):
    list_display = ['id','name','email','mob','add','password']


admin.site.register(vendor,ven_)


class order_(admin.ModelAdmin):
    list_display = ['id','userid','proid','mobile','add','paymenttype','transactionid','total','datetime']


admin.site.register(order,order_)

class regi_(admin.ModelAdmin):
    list_display = ['id','name','email','mob','add','password']

admin.site.register(register_new,regi_)

class Blog__(admin.ModelAdmin):
    list_display=['id','name','email']
    list_filter=['name','email']
    search_fields=['name','email']

admin.site.register(Blog,Blog__)