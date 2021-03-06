# from django.db import models

# # Create your models here.
# class Product(models.Model):
#     product_id = models.AutoField
#     product_name = models.CharField(max_length=50)
#     desc = models.CharField(max_length=300)
#     pub_date = models.DateField()

from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    # product_name = models.CharField(max_length=50)
    product_name = models.TextField()
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    # desc = models.TextField()
    desc=RichTextField(blank=True, null=True)
    pub_date = models.DateField()
    image = models.ImageField(upload_to='shop/images', default="")

    def __str__(self):
        return self.product_name
    objects = models.Manager() 

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")


    def __str__(self):
        return self.name

class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    amount =models.IntegerField(default=0)
    items_json = models.CharField(max_length=5000)
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=111)
    address = models.CharField(max_length=111)
    # city = models.CharField(max_length=111)
    # state = models.CharField(max_length=111)
    # zip_code = models.CharField(max_length=111)
    phone = models.CharField(max_length=111, default="")
    desc = models.CharField(max_length=100, default='')
    objects=models.Manager()



class OrderUpdate(models.Model):
    update_id  = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc
    objects=models.Manager()
# class OrderUpdate(models.Model):
#     update_id = models.AutoField(primary_key=True)    
#     order_id = models.IntegerField(default="")
#     update_desc= models.CharField(max_length=5000)
#     timestamp= models.DateField(auto_now=True) 
    

#     def __str__(self):
#         return self.update_desc[0:7] + "..." 
#                                            #is se sure ke 7 character ikhnge 
#                                                 #fir uske bad dot dot dikhnge 
#     objects = models.Manager()                                
