from django.contrib import admin
from apps.tickets.models import TypeTicket,TicketModel,Ticket,PaymentMethod,MethodsPaymentEvent,MethodsPaymentEventOffline
# Register your models here.
admin.site.register(PaymentMethod)
admin.site.register(TypeTicket)
admin.site.register(TicketModel)
admin.site.register(Ticket)
admin.site.register(MethodsPaymentEvent)
admin.site.register(MethodsPaymentEventOffline)
