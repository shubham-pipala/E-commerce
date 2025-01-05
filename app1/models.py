from django.db import models

# Create your models here.

class Blog1(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=50)
    content = models.TextField()


class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='catimg')

    def __str__(self):
        return self.name


class registeration(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mob = models.CharField(max_length=10)
    add = models.TextField()
    password = models.CharField(max_length=8)


class register_new(models.Model):
    name = models.CharField(max_length=50,blank=True,null=True)
    email = models.EmailField(blank=True,null=True)
    mob = models.CharField(max_length=10,blank=True,null=True)
    add = models.TextField(blank=True,null=True)
    password = models.CharField(max_length=8,blank=True,null=True)

    def __str__(self):
        return self.name
    
class product(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    stock = models.PositiveIntegerField()
    discription = models.TextField()
    image = models.ImageField(upload_to='proimg')
    category = models.ForeignKey(Category,on_delete=models.CASCADE)


class cart(models.Model):
    proid = models.CharField(max_length=5)
    qty = models.PositiveIntegerField()
    userid = models.CharField(max_length=5)
    orderid = models.CharField(max_length=10,default="0")
    totalprice = models.IntegerField(default=1)

    def __str__(self):
        return self.userid
    

class vendor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mob = models.CharField(max_length=10)
    add = models.TextField()
    password = models.CharField(max_length=8)

    def __str__(self):
        return self.name
    
import datetime

class order(models.Model):
    userid = models.ForeignKey(registeration,on_delete=models.CASCADE)
    proid = models.CharField(max_length=5)
    add = models.TextField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    mobile = models.CharField(max_length=10)
    pincode = models.CharField(max_length=6)
    paymenttype = models.CharField(max_length=50)
    total = models.PositiveIntegerField()
    transactionid = models.CharField(max_length=100)
    datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.pk)
    

class Blog(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)

    def _str_(self):
        return self.name


