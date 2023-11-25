from django.db import models
from django.contrib.auth.models import User
import datetime
import os
# Create your models here.
def get_file_path(request,filename):
    original_filename = filename
    nowtime = datetime.datetime.now().strftime('%d%m%y%H:%M:%S')
    filename ="%s%s" %(nowtime,original_filename)
    return os.path.join('uploads/',filename)



class Category(models.Model):
    slug = models.CharField(max_length=150,null=False,blank=False)
    name = models.CharField(max_length=150,null=False,blank=False)
    description = models.TextField(max_length=500,null=False,blank=False)
    image = models.ImageField(upload_to='get_file_path',null=True,blank=True)
    status = models.BooleanField(default=False,help_text='0=False,1=Hidden')
    trending = models.BooleanField(default=False,help_text='0=False,1=Trending')
    meta_title = models.CharField(max_length=150,null=False,blank=False)
    meta_keywords = models.CharField(max_length=150,null=False,blank=False)
    meta_description = models.TextField(max_length=500,null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    slug = models.CharField(max_length=150,null=False,blank=False)
    name = models.CharField(max_length=150,null=False,blank=False)
    small_description = models.CharField(max_length=150,null=False,blank=False)
    product_image = models.ImageField(upload_to='get_file_path',null=True,blank=True)
    quantity = models.IntegerField(null=False,blank=False)
    description = models.TextField(max_length=500,null=False,blank=False)
    original_price = models.FloatField(null=False,blank=False)
    selling_price = models.FloatField(null=False,blank=False)
    status = models.BooleanField(default=False,help_text='0=False,1=Hidden')
    trending = models.BooleanField(default=False,help_text='0=False,1=Trending')
    tag=models.CharField(max_length=150,null=False,blank=False)
    meta_title = models.CharField(max_length=150,null=False,blank=False)
    meta_keywords = models.CharField(max_length=150,null=False,blank=False)
    meta_description = models.TextField(max_length=500,null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
      return self.name


class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_qty = models.IntegerField(null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
      return self.product.name


class Wishlist(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
      return self.product.name



class Order(models.Model):
   user = models.ForeignKey(User,on_delete=models.CASCADE)
   fname  = models.CharField(max_length=150,blank=False, null=False)
   lname  = models.CharField(max_length=150,blank=False, null=False)
   email  = models.EmailField()
   Phone  = models.CharField(max_length=20,blank=False, null=False)
   address = models.TextField(null=False)
   country  = models.CharField(max_length=150,null=False)
   city = models.CharField(max_length=150,null=False)
   state  = models.CharField(max_length=150,null=False)
   pincode  = models.CharField(max_length=150,blank=False, null=False)
   total_price =models.FloatField(null=False)
   payment_mode = models.CharField(max_length=50,null=False)
   payment_id = models.CharField(max_length=50,null=False)
   orderstatus = (
      ('Pending','Pending'),
      ('Out of Shipping','Out of Shipping'),
      ('order delivered','order delivered')
   )
   status =models.CharField(max_length=50,null=False, choices=orderstatus,default='Pending')
   message = models.TextField(max_length=150,null= True)
   tracking_no = models.CharField(max_length=50,null=True)
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now_add=True)

   def __str__(self):
      return '{} - {}'.format(self.id ,self.tracking_no)




class OrderItem(models.Model):
   order = models.ForeignKey(Order,on_delete=models.CASCADE)
   product = models.ForeignKey(Product,on_delete=models.CASCADE)
   price = models.FloatField(null =False)
   quantity = models.IntegerField(null = False)

   def __str__(self):
      return '{} - {}'.format(self.order.id ,self.order.tracking_no)



class Profile(models.Model):
   user = models.ForeignKey(User,on_delete=models.CASCADE)
   Phone  = models.CharField(max_length=20,blank=False, null=False)
   address = models.TextField(null=False)
   country  = models.CharField(max_length=150,null=False)
   city = models.CharField(max_length=150,null=False)
   state  = models.CharField(max_length=150,null=False)
   pincode  = models.CharField(max_length=150,blank=False, null=False)

   def __str__(self):
      return self.user.username
   