from django.contrib import admin
from .models import Category,Product,Cart,CartItem,Order,OrderItem,ProductImages,Review,ShippingAddress,OrderPayment,UserProfile
from django.utils.html import format_html

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name',]
admin.site.register(Category,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','description','display_image','category','price','stock']
    def display_image(self,obj):
        if obj.image:
            return format_html('<img src="{}" width="100px" heigth="100px" />',obj.image.url)
        return None 
    display_image.short_descriptions = 'Image'
admin.site.register(Product,ProductAdmin)

class CartAdmin(admin.ModelAdmin):
    list_display = ['user',]
admin.site.register(Cart,CartAdmin)

class CartItemAdmin(admin.ModelAdmin):
    list_display = ['cart','products','quantity',]
admin.site.register(CartItem,CartItemAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ['user',]
admin.site.register(Order,OrderAdmin)

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order','product','quantity',]
admin.site.register(OrderItem,OrderItemAdmin)

class ProductImagesAdmin(admin.ModelAdmin):
    list_display = ['product','image1','image2','image3',]
admin.site.register(ProductImages,ProductImagesAdmin)

class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user','product','rating','review','date',]
admin.site.register(Review,ReviewAdmin)


class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ['user','name','address','city','state','zip_code']
admin.site.register(ShippingAddress,ShippingAddressAdmin)

admin.site.register(OrderPayment)
admin.site.register(UserProfile)