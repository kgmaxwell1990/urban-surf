from __future__ import unicode_literals

from django.db import models
from products.models import Products
from django.contrib.auth.models import User

class CartItem(models.Model):
    user = models.ForeignKey(User)
    product = models.ForeignKey(Products)
    quantity = models.IntegerField(default=1)
    size = models.CharField(max_length=2)

    def __str__(self):
        return "{0} ({1})".format(self.product.name, self.quantity, self.size)
