from django.contrib.auth.models import User
from django.db import models
from apps.events.models import EventModel
from apps.event_planner.models import ShellerModel
from datetime import datetime

class PaymentMethod(models.Model):
    title = models.CharField(max_length=60,null=False,blank=False)
    description = models.CharField(max_length=255,null=False,blank=False)
    image = models.ImageField(upload_to='images_methods/',null=True,blank=True)

    def __str__(self):
        return '{}'.format(self.title)


class MethodsPaymentEvent(models.Model):
    event = models.ForeignKey(EventModel, on_delete=models.CASCADE)
    method = models.ForeignKey(PaymentMethod,on_delete=models.CASCADE)
    key_one = models.CharField(max_length=200,null=True,blank=True)
    ket_two = models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return '{} {}'.format(self.event.title,self.method.title)

class MethodsPaymentEventOffline(models.Model):
    image = models.ImageField(upload_to='images_methods/',null=True,blank=True)
    event = models.ForeignKey(EventModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=200,null=False,blank=False)
    description = models.TextField(max_length=250,null=False,blank=False)
    message = models.TextField(max_length=250,null=False,blank=False)

class TypeTicket(models.Model):
    title = models.CharField(max_length=80,null=False,blank=False)
    description = models.TextField(max_length=80,null=False,blank=False)

    def __str__(self):
        return '{}'.format(self.title)

class TicketModel(models.Model):
    title = models.CharField(max_length=150,blank=False,null=False)
    quantity = models.IntegerField()
    price = models.FloatField()
    description = models.TextField(max_length=500,blank=False,null=False)
    start_sales_date = models.DateField()
    start_sales_time = models.TimeField()
    end_sales_date = models.DateField()
    end_sales_time = models.TimeField()
    number_tickets_order_min = models.IntegerField()
    number_tickets_order_max = models.IntegerField()
    visibility = models.BooleanField()
    start_visibility_date = models.DateField(null=True,blank=True)
    start_visibility_time = models.TimeField(null=True,blank=True)
    end_visibility_date = models.DateField(null=True,blank=True)
    end_visibility_time = models.TimeField(null=True,blank=True)
    event = models.ForeignKey(EventModel,on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.title)

class Ticket(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    info_ticket = models.ForeignKey(TicketModel,on_delete=models.CASCADE)
    payment_method = models.ForeignKey(PaymentMethod,on_delete=models.CASCADE)
    sheller = models.ForeignKey(ShellerModel,null=True,blank=True,on_delete=models.CASCADE)
    date = models.DateTimeField(blank=True, default=datetime.now())

    def __str__(self):
        return '{} {} - {} - {}'.format(self.user.first_name,self.user.last_name,self.info_ticket.title,self.info_ticket.event.title)
