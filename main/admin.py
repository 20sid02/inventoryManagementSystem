from django.contrib import admin
from . import models

admin.site.register(models.products)
admin.site.register(models.inventory)
admin.site.register(models.inventory_transactions)
