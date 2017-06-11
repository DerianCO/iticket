from django.db import models

# Create your models here.
class ConfigPlatform(models.Model):
    title = models.CharField(max_length=80,null=False,blank=False)
    logo = models.ImageField(upload_to="config_platform/")
    color_one = models.CharField(blank=True,null=True, max_length=8)
    color_two = models.CharField(blank=True,null=True, max_length=8)
    color_three = models.CharField(blank=True,null=True, max_length=8)
    banner_one = models.ImageField(upload_to="config_platform/")
    banner_two = models.ImageField(upload_to="config_platform/")
    video_id = models.CharField(blank=True, null=True,max_length=30)
    phone = models.CharField(blank=True,null=True,max_length=20)
    email = models.EmailField(blank=True,null=True,max_length=40)
    
    def __str__(self):
        return '{}'.format(self.title)
