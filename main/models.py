from django.db import models
from django.core.exceptions import ValidationError

class products(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128, null=False, blank=False)
    sku = models.CharField(max_length=50, unique=True, null=False)
    cost_price = models.DecimalField(max_digits=12, decimal_places=2, null=False, blank=False)
    selling_price = models.DecimalField(max_digits=12, decimal_places=2, null=False, blank=False)
    reorder_level = models.IntegerField(default=10)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.sku})"



class inventory(models.Model):
    inventory_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(products, on_delete=models.CASCADE, null=False, blank=False)
    quantity = models.PositiveIntegerField(default=0, null=False, blank=False)
    last_updated = models.DateTimeField(auto_now_add=True)



class inventory_transactions(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(products, on_delete=models.CASCADE, null=False, blank=False)
    change_type = models.CharField(max_length=10, choices=[('IN', 'In'), ('OUT', 'Out')])
    quantity = models.PositiveIntegerField(default=0, null=False, blank=False)
    passed = models.BooleanField(default=True)
    timestamp = models.DateField(auto_now_add=True)
"""
    def save(self, *args, **kwargs):
        creating = self._state.adding
        super().save(*args, **kwargs)

        if creating:
            inv, _ = inventory.objects.get_or_create(product=self.product)

            if self.change_type == 'IN':
                inventory.objects.filter(product=self.product).update(
                quantity=models.F("quantity") + self.quantity
            )
            
            else:
                if inv.quantity - self.quantity < 0:
                    raise ValidationError('Not Enough Stock available')
                inventory.objects.filter(product=self.product).update(
                quantity=models.F("quantity") - self.quantity
            )

            inv.refresh_from_db()

"""

