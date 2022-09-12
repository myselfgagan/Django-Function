from django.urls import reverse
from turtle import title
from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=20)
    featured = models.BooleanField(default=True)

    def get_absolute_url(self):
        return f"/lookup/{self.id}"


        # URLs reverse
        # return reverse("products:detail-product", kwargs={"id": self.id})    ---> this is not working