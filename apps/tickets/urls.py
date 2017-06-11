from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from apps.tickets.views import getTickets,sellTicket

urlpatterns = [
    url(r'^forevent/$', login_required(getTickets), name='gettickets'),
    url(r'^sell/$', login_required(sellTicket), name='sellticket'),
]
