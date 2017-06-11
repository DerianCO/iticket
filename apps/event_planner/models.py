from django.contrib.auth.models import User
from django.db import models
from apps.events.models import EventModel
# Create your models here.
class EventPlannerModel(models.Model):
    name = models.CharField(max_length=120, null=False,blank=False)
    image = models.ImageField(upload_to='images_planners/')
    description = models.TextField(max_length=255,null=False,blank=False)
    twitter = models.TextField(max_length=150,null=True,blank=True)
    facebook = models.TextField(max_length=150,null=True,blank=True)
    event = models.ForeignKey(EventModel,on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.name)

class SponsorModel(models.Model):
    title = models.CharField(max_length=100, null=False,blank=False)
    logo = models.ImageField(upload_to='sponsors_logos/')
    event = models.ForeignKey(EventModel,on_delete=models.CASCADE)
    def __str__(self):
        return '{}'.format(self.title)

class GuestsModels(models.Model):
    name = models.CharField(max_length=100,null=False,blank=False)
    image = models.ImageField(upload_to='images_guests/')
    twitter = models.CharField(max_length=50,null=True,blank=True)
    facebook = models.CharField(max_length=80,null=True,blank=True)
    event = models.ForeignKey(EventModel,on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.name)

class ShellersGroupModel(models.Model):
    title = models.CharField(max_length=100,null=False,blank=False)
    event = models.ForeignKey(EventModel,on_delete=models.CASCADE)
    boss = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.title)

class ShellerModel(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    group = models.ForeignKey(ShellersGroupModel,on_delete=models.CASCADE)

    def __str__(self):
        return 'Vendedor {}'.format(self.user.username)
