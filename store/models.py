from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


"""
creating models and Category to record 
"""
class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    """
in order to get the catogory need to type the slug

"""
    slug= models.SlugField(max_length=255,unique=True)
    """
 meta data ,data about deta more details abbout data
"""
    class Meta:
       verbose_name_plural = 'catagories'


    def __str__(self):
        return self.name

"""
creating product tables and connect that to the table with foreignKey
"""
class Product(models.Model):
    Category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    """
    who can creted the product 
    """
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_creator')
    """
    create title for the product nad owner for the product
    """
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, default='admin')
    """
    product description 
    """
    description= models.TextField(blank=True)

    """
    upload image
        """
    image = models.ImageField(upload_to = 'images/')
    slug = models.SlugField(max_length=255)
    """
    add price and in stock
    """
    price = models.DecimalField(max_digits=4,decimal_places=2)
    in_stock= models.BooleanField(default=True)

    """
    all new product created and updated
        """
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Products'
    
        """
        showing data eceding order ,or placed in the data base
        """
        ordering = ('-created',)
        """
    show default string of the title(title of the data)
    """
    def ___str__(self):
        return self.title


   
          

    



