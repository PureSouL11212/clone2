from django.contrib import admin
from .models import Product
# Register your models here.
from .models import Bills
admin.site.register(Bills)
admin.site.register(Product)
