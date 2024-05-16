from django.db import models
from django.contrib.auth.models import User

class Cryptocurrency(models.Model):
    name = models.CharField(max_length=50)
    symbol = models.CharField(max_length=10, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def _str_(self):
            return self.name

class Portfolio(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cryptocurrencies = models.ManyToManyField(Cryptocurrency)

    def _str_(self):
        return f"{self.user.username}'s {self.cryptocurrencies.name} ({self.cryptocurrencies.symbol})"



    