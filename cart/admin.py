from django.contrib import admin

# Register your models here.
from cart.models import Cart, CartProduct

admin.site.register(Cart)
admin.site.register(CartProduct)