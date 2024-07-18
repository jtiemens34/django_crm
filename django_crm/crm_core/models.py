from django.db import models

# Create your models here.
class Customer(models.Model):
  first_name = models.TextField(max_length=14)
  last_name = models.TextField(max_length=14)
  email = models.TextField()
  phone = models.TextField()
  city = models.TextField()
  def __str__(self):
    return self.first_name + " " + self.last_name