from django.contrib.auth.models import User
from django.db import models

class TypeEventModel(models.Model):
    tile = models.CharField(max_length=80,null=False,blank=False)
    description = models.TextField(max_length=255, null=False,blank=False)
    icon = models.TextField(max_length=255,null=True,blank=True)

    def __str__(self):
        return '{}'.format(self.tile)

class TypeLocation(models.Model):
    title = models.CharField(max_length=80,null=False,blank=False)
    description = models.TextField(max_length=255,null=False,blank=False)
    def __str__(self):
        return '{}'.format(self.title)

class EventModel(models.Model):
    title = models.CharField(max_length=80,null=False,blank=False)
    status = models.BooleanField(default=False)
    location_type = models.ForeignKey(TypeLocation,on_delete=models.CASCADE)
    location_name = models.CharField(max_length=200,null=True,blank=True)
    location_address = models.CharField(max_length=200,null=True,blank=True)
    location_address_latitude = models.CharField(max_length=30,blank=True,null=True)
    location_address_longitude = models.CharField(max_length=30,blank=True,null=True)
    location_address_two = models.CharField(max_length=200,null=True,blank=True)
    location_address_two_latitude = models.CharField(max_length=30,blank=True,null=True)
    location_address_two_longitude = models.CharField(max_length=30,blank=True,null=True)
    location_state = models.CharField(max_length=150,null=True,blank=True)
    location_postal_code = models.CharField(max_length=12,null=True,blank=True)
    location_country = models.CharField(max_length=150,null=True,blank=True)
    url_event = models.CharField(max_length=180,null=True,blank=True)
    show_map = models.BooleanField()
    start_date = models.DateField()
    start_time = models.TimeField()
    end_date = models.DateField()
    end_time = models.TimeField()
    description = models.TextField(max_length=600,null=False,blank=False)
    privacy = models.BooleanField()
    show_tickets_remaining = models.BooleanField()
    type_event = models.ForeignKey(TypeEventModel,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def publish(self):
        if self.status == False:
            self.status = True
            self.save()
        else:
            self.status = False
            self.save()

    def change_showmap(self):
        if self.show_map == False:
            self.show_map = True
            self.save()
        else:
            self.show_map = False
            self.save()

    def change_privacy(self):
        if self.privacy == True:
            self.privacy = False
            self.save()
        else:
            self.privacy = True
            self.save()

    def change_tickets_remaining(self):
        if self.show_tickets_remaining == False:
            self.show_tickets_remaining = True
            self.save()
        else:
            self.show_tickets_remaining = False
            self.save()

    def __str__(self):
        return '{}'.format(self.title)


class ImagesEvent(models.Model):
    image = models.ImageField(upload_to='images_events/')
    event = models.ForeignKey(EventModel, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.image.url)

class GalleryEvent(models.Model):
    image = models.ImageField(upload_to='gallery_events/')
    event = models.ForeignKey(EventModel,on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.image.url)


class EventSchedule(models.Model):
    title = models.CharField(max_length=50, null=False,blank=False)
    start_date = models.DateField(null=False,blank=False)
    start_time = models.TimeField(null=False,blank=False)
    end_date = models.DateField(null=False,blank=False)
    end_time = models.TimeField(null=False,blank=False)
    image = models.ImageField(upload_to='schedule_events/')
    event = models.ForeignKey(EventModel,on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.title)

class RequestAssistance(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    event = models.ForeignKey(EventModel,on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    def toAccept(self):
        self.status = True
        self.save()


class EventQualification(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    event = models.ForeignKey(EventModel,on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
