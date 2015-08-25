from django.contrib import admin
from .models import Address, Country


admin.site.register(Country)
admin.site.register(Address)
