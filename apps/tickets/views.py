from django.shortcuts import render

from django.contrib.auth.models import User

from apps.tickets.models import Ticket,TicketModel,PaymentMethod
from apps.event_planner.models import ShellerModel,ShellersGroupModel

from django.http.response import JsonResponse, HttpResponse
from django.shortcuts import render, redirect

# Create your views here.

def getTickets(request):
    if request.method == 'POST':
        tickets = TicketModel.objects.filter(event__id=request.POST.get('idEvent'))
        tickets_return = []

        for ticket in tickets:
            tickets_return.append({
                'title':ticket.title,
                'price':ticket.price,
                'id': ticket.id
            })

        return JsonResponse({
            'tickets' : tickets_return
        })

def sellTicket(request):
    if request.method == 'POST':
        user = User.objects.get(id=request.POST.get('idUser'))

        info_ticket = TicketModel.objects.get(id=request.POST.get('idInfo'))

        payment_method = PaymentMethod.objects.get(id=request.POST.get('idMethod'))

        sheller = ShellerModel.objects.get(id=request.POST.get('idSheller'))

        ticket_new = Ticket.objects.create(user=user,info_ticket=info_ticket,payment_method=payment_method,sheller=sheller)

        return JsonResponse({
            'status' : 'OK',
            'idnewticket': ticket_new.id,
            'username' : user.username,
            'email' : user.email,
        })
