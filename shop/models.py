from django.db import models




# Create your models here.
class Products(models.Model):
  
  def __str__(self):
    return self.title
  title = models.CharField(max_length=200)
  price = models.FloatField()
  discount_price = models.FloatField()
  category = models.CharField(max_length=200)
  description = models.TextField()
  image = models.CharField(max_length=1000000)
  image2 = models.CharField(max_length=1000000)
  image3 = models.CharField(max_length=1000000)
  

class Order(models.Model):

  items = models.CharField(max_length=1000)
  name = models.CharField(max_length=200)
  city = models.CharField(max_length=200)
  email = models.EmailField(max_length=200)
  zipcode = models.CharField(max_length=200)
  state = models.CharField(max_length=200)
  address = models.CharField(max_length=200)
  total = models.CharField(max_length=200)

class PostImage(models.Model):
  post = models.ForeignKey(Products, default=None, on_delete=models.CASCADE)
  images = models.ImageField(upload_to = 'images/')
 
  def __str__(self):
    return self.post.title