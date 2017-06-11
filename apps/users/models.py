from django.contrib.auth.models import User
from django.db import models
from apps.events.models import TypeEventModel

class UserInfoModel(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image_profile = models.ImageField(upload_to='image_profile/',null=True,blank=True)
    home_phone = models.CharField(max_length=20,null=True,blank=True)
    cell_phone = models.CharField(max_length=30, null=True,blank=True)
    job_title = models.CharField(max_length=100, null=True,blank=True)
    company = models.CharField(max_length=100, null=True,blank=True)
    website = models.CharField(max_length=255,null=True,blank=True)
    blog = models.CharField(max_length=255,null=True,blank=True)
    address = models.CharField(max_length=150,null=True,blank=True)
    address_two = models.CharField(max_length=150,null=True,blank=True)
    city = models.CharField(max_length=30,null=True,blank=True)
    country = models.CharField(max_length=40,null=True,blank=True)
    postal_code = models.IntegerField(null=True,blank=True)
    address_billing = models.CharField(max_length=150, null=True, blank=True)
    address_two_billing = models.CharField(max_length=150, null=True, blank=True)
    city_billing = models.CharField(max_length=30, null=True, blank=True)
    country_billing = models.CharField(max_length=40, null=True, blank=True)
    postal_code_billing = models.IntegerField(null=True, blank=True)
    address_shipping = models.CharField(max_length=150, null=True, blank=True)
    address_two_shipping = models.CharField(max_length=150, null=True, blank=True)
    city_shipping = models.CharField(max_length=30, null=True, blank=True)
    country_shipping = models.CharField(max_length=40, null=True, blank=True)
    postal_code_shipping = models.IntegerField(null=True, blank=True)
    address_work = models.CharField(max_length=150, null=True, blank=True)
    address_two_work = models.CharField(max_length=150, null=True, blank=True)
    city_work = models.CharField(max_length=30, null=True, blank=True)
    country_work = models.CharField(max_length=40, null=True, blank=True)
    postal_code_work = models.IntegerField(null=True, blank=True)
    birth_date = models.DateField(null=True,blank=True)
    age = models.IntegerField(null=True,blank=True)
    preferences = models.ManyToManyField(TypeEventModel)

    def __str__(self):
        return '{} {}'.format(self.user.first_name,self.user.last_name)
