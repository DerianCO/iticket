from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.http.response import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.utils.timezone import now
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from apps.event_planner.forms import SponsorModelForm, EventPlannerModelForm, GuestModelForm,ShellerModelForm,ShellersGroupModelForm
from apps.events.models import EventModel,ImagesEvent,EventSchedule,TypeEventModel,TypeLocation, GalleryEvent, EventSchedule,RequestAssistance
from apps.events.forms import EventForm, ImagesEventForm, GalleryEventForm, EventScheduleForm

from apps.event_planner.models import EventPlannerModel,GuestsModels,SponsorModel,ShellersGroupModel,ShellerModel
from apps.tickets.forms import TicketModelForm,MethodsPaymentEventOfflineForm
from apps.configplatform.models import ConfigPlatform

from apps.tickets.models import TicketModel,Ticket,MethodsPaymentEvent,PaymentMethod,MethodsPaymentEventOffline

# Create your views here.

def visibility(ticket):
    if (ticket.start_visibility_date < now().date() and ticket.end_visibility_date > now().date()):
        return True
    elif (ticket.start_visibility_date < now().date() and ticket.end_visibility_date == now().date()):
        if (ticket.end_visibility_time > now().time()):
            return True
    elif (ticket.start_visibility_date == now().date() and ticket.end_visibility_date > now().date()):
        if (ticket.start_visibility_time < now().time()):
            return True
    elif (ticket.start_visibility_date == now().date() and ticket.end_visibility_date == now().date()):
        if (ticket.start_visibility_time < now().time() and ticket.end_visibility_time > now().time()):
            return True
    else:
        return False


def EventView(request,view,idevent):
    config = ConfigPlatform.objects.get(id=1)
    if (EventModel.objects.filter(id=idevent).exists()):
        event = EventModel.objects.filter(id=idevent).first()
        if(event.status and TicketModel.objects.filter(event=event).exists() and ImagesEvent.objects.filter(event=event).exists()):
            event_planner = EventPlannerModel.objects.filter(event=event)
            tickets = TicketModel.objects.filter(event=event)
            images = ImagesEvent.objects.filter(event=event)
            guests = GuestsModels.objects.filter(event=event)
            sponsors = SponsorModel.objects.filter(event=event)
            schedules = EventSchedule.objects.all().order_by('start_date','start_time')
            gallery = GalleryEvent.objects.filter(event=event)
            type_events = TypeEventModel.objects.all()

            tickets_view = []
            for ticket in tickets:
                if(ticket.start_sales_date<now().date() and ticket.end_sales_date>now().date()):
                    if(ticket.visibility or  visibility(ticket)):
                        tickets_view.append(ticket)
                elif(ticket.start_sales_date<now().date() and ticket.end_sales_date==now().date()):
                    if(ticket.end_sales_time>now().time()):
                        if (ticket.visibility or visibility(ticket)):
                            tickets_view.append(ticket)
                elif (ticket.start_sales_date == now().date() and ticket.end_sales_date > now().date()):
                    if(ticket.start_sales_time<now().time()):
                        if (ticket.visibility or visibility(ticket)):
                            tickets_view.append(ticket)
                elif (ticket.start_sales_date == now().date() and ticket.end_sales_date == now().date()):
                    if(ticket.start_sales_time<now().time() and ticket.end_sales_time > now().time()):
                        if (ticket.visibility or visibility(ticket)):
                            tickets_view.append(ticket)

            if request.user.username:
                UserRequestAssistance = RequestAssistance.objects.filter(user=request.user).first()

                if UserRequestAssistance and UserRequestAssistance.status or event.user == request.user:
                    ra = True
                else:
                    ra = False

                if event.user == request.user:
                    admin = True
                else:
                    admin = False
            else:
                ra = False
                admin = False

            context = {
             'event' : event,
             'planner' : event_planner,
             'tickets' : tickets,
             'tickets_view' : tickets_view,
             'now' : now(),
             'images' : images,
             'guests' : guests,
             'sponsors' : sponsors,
             'schedules' : schedules,
             'gallery' : gallery,
             'config' : config,
             'request_assistance': ra,
             'admin' : admin,
             'type_events' : type_events,
            }

            if(view == 'home'):
                return render(request, 'event/event_view_home.html', context)
        else:
            return HttpResponse('404')
    else:
        return HttpResponse('404')


def ReqAssistance(request):
    if request.method == 'POST':
        event = EventModel.objects.get(id=request.POST.get("event_id"))
        user = request.user
        request_assistance = RequestAssistance.objects.filter(user=user,event=event).first()
        if request_assistance:
            return JsonResponse({
                'status' : True
            })
        else:
            req = RequestAssistance(user=user,event=event)
            req.save()

            return JsonResponse({
                'status' : True
            })

def Home(request):
    data = []
    events = EventModel.objects.all().order_by('start_date')
    type_events = TypeEventModel.objects.all()
    config = ConfigPlatform.objects.get(id=1)
    for event in events:
        if event.status and event.location_type.id == 2:
            if(TicketModel.objects.filter(event=event).exists()):
                if(ImagesEvent.objects.filter(event=event).exists()):
                    ticket = TicketModel.objects.filter(event=event).order_by('price').first()
                    image = ImagesEvent.objects.filter(event=event).first()

                    data.append({
                        'event': event,
                        'ticket': ticket,
                        'image': image,
                    })

    return render(request,'home/index.html', context={'data': data,'type_events':type_events, 'config':config})

def getEvents(request):
    if request.method == 'POST':
        type_id = int(request.POST.get('type_id'))
        events_response = []
        if(type_id != 0):
            events = EventModel.objects.filter(type_event__id=type_id)
        else:
            events = EventModel.objects.all()

        for event in events:
            if event.status:
                events_response.append({
                    'title':event.title
                })

        return JsonResponse({'events':events_response})

def CreateEvent(request):
    if request.method == 'GET':
        type_events = TypeEventModel.objects.all()
        type_location = TypeLocation.objects.all()
        config = ConfigPlatform.objects.get(id=1)

        return render(request,'event/event_new.html',context={'type_events':type_events,'type_location':type_location,'config':config})
    elif request.method == 'POST':

        if request.POST.get('idevent'):
            event = EventModel.objects.filter(id=request.POST.get('idevent')).first()
            event.title = request.POST.get('title')
            event.url_event = request.POST.get('url_event')
            event.description = request.POST.get('description')
            event.type_event = TypeEventModel.objects.get(id=request.POST.get('id_type'))
            event.location_name = request.POST.get('locationName')
            event.location_address = request.POST.get('locationAddress')
            event.location_state = request.POST.get('locationState')
            event.location_country = request.POST.get('locationCountry')
            event.save()

            return JsonResponse({
                'status' : "change",
            })
        else:
            form = EventForm(request.POST)

            if form.is_valid():
                event = form.save(commit=False)
                event.user = User.objects.filter(id=request.user.id).first()
                newevent = form.save()

                return JsonResponse({
                    'status' : "OK",
                    'id_event' : newevent.id,
                })
            else:
                return JsonResponse({
                    'status' : "Error",
                    'errors' : form.errors,
                })

            #return redirect('events:dashboard',newevent.id)

def DashboardEvent(request,idevent):
    if request.method == 'GET':
        type_events = TypeEventModel.objects.all()
        event = EventModel.objects.filter(id=idevent).first()
        tickets = TicketModel.objects.filter(event=event).order_by('price')
        images= ImagesEvent.objects.filter(event=event)
        shellers = ShellersGroupModel.objects.filter(event=event)
        guests = GuestsModels.objects.filter(event=event)
        planners = EventPlannerModel.objects.filter(event=event)
        gallery = GalleryEvent.objects.filter(event=event)
        sponsors = SponsorModel.objects.filter(event=event)
        schedules = EventSchedule.objects.filter(event=event)
        config = ConfigPlatform.objects.get(id=1)
        request_assistance = RequestAssistance.objects.filter(event=event,status=False)

        if(request.user == event.user):
            context = {
                'event': event,
                'tickets':tickets,
                'images':images,
                'config':config,
                'type_events':type_events,
                'assistance':request_assistance,
                'shellers' : shellers,
                'guests' : guests,
                'planners' : planners,
                'gallery' : gallery,
                'sponsors' : sponsors,
                'schedules' : schedules,
            }

            return render(request, 'event/event_dashboard.html', context)
        else:
            return  HttpResponse('profile:home',request.user.id)

def EventImages(request,idevent):
     return Create(request,idevent,ImagesEvent,ImagesEventForm,'events:event_images','event/event_images.html')

def EventGallery(request,idevent):
     return Create(request,idevent,GalleryEvent,GalleryEventForm,'events:event_gallery','event/event_gallery.html')

def EventTicket(request,idevent):
     return Create(request,idevent,TicketModel,TicketModelForm,'events:event_tickets','event/event_tickets.html')

def EventPlanner(request,idevent):
     return Create(request,idevent,EventPlannerModel,EventPlannerModelForm,'events:event_planners','event/event_planners.html')

def EventSponsor(request,idevent):
    return Create(request,idevent,SponsorModel,SponsorModelForm,'events:event_sponsors','event/event_sponsors.html')

def EventGuest(request,idevent):
    return Create(request,idevent,GuestsModels,GuestModelForm,'events:event_guests','event/event_guests.html')

def EventSchedules(request,idevent):
    return Create(request,idevent,EventSchedule,EventScheduleForm,'events:event_schedules','event/event_schedules.html')

def EventMethodsPaymentEventOffline(request,idevent):
    if request.method == 'POST':
        form_post = MethodsPaymentEventOfflineForm(request.POST,request.FILES)
        if form_post.is_valid():
            form_create = form_post.save(commit=False)
            form_create.event = EventModel.objects.filter(id=idevent).first()
            form_create.save()
        return redirect('events:event_configurations',idevent)

def EventShellers(request,idevent):
    model = ShellersGroupModel
    form = ShellersGroupModelForm

    if request.method == 'GET':
        event = EventModel.objects.filter(id=idevent).first()
        type_events = TypeEventModel.objects.all()
        config = ConfigPlatform.objects.get(id=1)
        model_create = model.objects.filter(event__id=idevent)
        model_form = form
        users = User.objects.all()

        groups_shellers=[]

        for group in model_create:
            shellers = ShellerModel.objects.filter(group=group)
            groups_shellers.append({
                'group' : group,
                'shellers' : shellers
            })

        context = {
            'model':groups_shellers,
            'form':model_form,
            'event':event,
            'config':config,
            'type_events':type_events,
            'users':users
        }

        if request.user == event.user:
            return  render(request,'event/event_shellers.html', context )
        else:
            return redirect('profile:home', request.user.username)
    elif request.method == 'POST':
        form_post = form(request.POST,request.FILES)
        if form_post.is_valid():
            form_create = form_post.save(commit=False)
            form_create.event = EventModel.objects.filter(id=idevent).first()
            form_create.save()
        return redirect('events:event_shellers',idevent)


def EventConfigurations(request,idevent):
    if request.method == 'GET':
        event = EventModel.objects.filter(id=idevent).first()
        type_events = TypeEventModel.objects.all()
        config = ConfigPlatform.objects.get(id=1)
        methodsevent = MethodsPaymentEvent.objects.filter(event=event)
        methods = PaymentMethod.objects.all()
        methodsevent_offline = MethodsPaymentEventOffline.objects.filter(event=event)
        form_offline = MethodsPaymentEventOfflineForm
        context = {
            'methodspaymentevent' : methodsevent,
            'event':event,
            'config':config,
            'type_events':type_events,
            'paymentmethods': methods,
            'form_offline' : form_offline,
            'methodspaymenteventoffline' : methodsevent_offline,
        }

        if request.user == event.user:
            return  render(request,'event/event_configurations.html', context )
        else:
            return redirect('profile:home', request.user.username)

def configPlatformPayment(request):
    if request.method == 'POST':
        event = EventModel.objects.get(id=request.POST.get('idevent'))
        method = PaymentMethod.objects.get(id=request.POST.get('method'))
        if request.POST.get('idmpeo'):
            config = MethodsPaymentEvent.objects.get(id=request.POST.get('idmpeo'))
            config.key_one = request.POST.get('key_one')
            config.ket_two = request.POST.get('ket_two')
            config.save()

            return JsonResponse({
                'status' : 'change'
            })

        else:
            new_config = MethodsPaymentEvent.objects.create(event=event,method=method,key_one = request.POST.get('key_one'), ket_two = request.POST.get('ket_two'))

            return JsonResponse({
                'status' : 'OK'
            })

def Create(request,idevent,modelc,formc,urlc,template):
    model = modelc
    form = formc

    if request.method == 'GET':
        event = EventModel.objects.filter(id=idevent).first()
        type_events = TypeEventModel.objects.all()
        config = ConfigPlatform.objects.get(id=1)
        model_create = model.objects.filter(event__id=idevent)
        model_form = form

        if request.user == event.user:
            return  render(request,template, context={'model':model_create,'form':model_form,'event':event,'config':config,'type_events':type_events})
        else:
            return redirect('profile:home', request.user.username)
    elif request.method == 'POST':
        form_post = form(request.POST,request.FILES)
        if form_post.is_valid():
            form_create = form_post.save(commit=False)
            form_create.event = EventModel.objects.filter(id=idevent).first()
            form_create.save()
        return redirect(urlc,idevent)

def Delete(request,idevent):
    if request.method == 'POST':
        id_model = request.POST.get('id_model')

        if request.POST.get('model') == 'planner':
            model = EventPlannerModel.objects.filter(id=id_model).first()

        elif request.POST.get('model') == 'sponsor':
            model = SponsorModel.objects.filter(id=id_model).first()

        elif request.POST.get('model') == 'guest':
            model = GuestsModels.objects.filter(id=id_model).first()

        elif request.POST.get('model') == 'ticket':
            model = TicketModel.objects.filter(id=id_model).first()

        elif request.POST.get('model') == 'image':
            model = ImagesEvent.objects.filter(id=id_model).first()

        elif request.POST.get('model') == 'gallery':
            model = GalleryEvent.objects.filter(id=id_model).first()

        elif request.POST.get('model') == 'schedule':
            model = EventSchedule.objects.filter(id=id_model).first()

        elif request.POST.get('model') == 'sheller':
            model = ShellerModel.objects.filter(id=id_model).first()

        elif request.POST.get('model') == 'mpeo':
            print('prueba')
            model = MethodsPaymentEventOffline.objects.filter(id=id_model).first()

        model.delete()

        ReadyEvent(idevent)

        return JsonResponse({
            'Status' : 'delete',
            'id' : id_model,
        })


def destroyEvent(request):
    if request.method == 'POST':
        idevent = request.POST.get('idEvent')
        event = EventModel.objects.filter(id=idevent)
        event.delete()

        return JsonResponse({
            'status' : 'delete',
            'id' : idevent,
        })

def ReadyEvent(idevent):
    event = EventModel.objects.filter(id=idevent).first()
    images = ImagesEvent.objects.filter(event=event)
    tickets = TicketModel.objects.filter(event=event)
    if ((images.count()>0 and tickets.count()>0)==False):
        event.publish()

def PublishEvent(request,idevent):
    if request.method == 'GET':
        event = EventModel.objects.filter(id=idevent).first()
        if request.user == event.user:
            event.publish()
            return redirect('events:dashboard', idevent)

def GetStatsTickets(request):
    if request.method == 'POST':
        title = []
        quantity = []
        money = []
        total = 0
        tickets = TicketModel.objects.filter(event__id=request.POST.get('id_event'))

        for ticket in tickets:
            ticket_sold = Ticket.objects.filter(info_ticket=ticket)
            count_tickets_sold = ticket_sold.count()
            quantity_money = count_tickets_sold * ticket.price

            title.append(ticket.title)
            quantity.append(count_tickets_sold)
            money.append(quantity_money)
            total += quantity_money


        return JsonResponse({'titles':title,'quantity':quantity,'money':money,'total':total})

def TicketsSold(request):
    if request.method == 'POST':
        tickets_sold_list = []
        tickets = TicketModel.objects.filter(event__id=request.POST.get('id_event'))
        for ticket in tickets:
            tickets_sold = Ticket.objects.filter(info_ticket=ticket).order_by('date')
            for ts in tickets_sold:
                tickets_sold_list.append({
                    'user':ts.user.username,
                    'ticket': ts.info_ticket.title,
                    'price' : ts.info_ticket.price,
                    'method' : ts.payment_method.title,
                    'date' : ts.date,
                })

        return JsonResponse({'tickets_sold_list':tickets_sold_list})

def toAccept(request):
    if request.method == 'POST':
         request_assistance = RequestAssistance.objects.filter(id=request.POST.get('idRequestAssistance')).first()
         request_assistance.toAccept()

         return JsonResponse({'status':'OK','idRequestAssistance':request_assistance.id})


def addShellerInTheGroup(request):
    if request.method == 'POST':
        user = User.objects.filter(id=request.POST.get('idUser')).first()
        group = ShellersGroupModel.objects.filter(id=request.POST.get('idGroup')).first()

        new_sheller = ShellerModel.objects.create(user=user,group=group)

        return JsonResponse({
            'status' : 'OK',
            'idSheller' : new_sheller.id,
            'idGroup' : group.id,
            'username' : user.username,
            'last_name' : user.last_name,
            'first_name' : user.first_name,
            'email' : user.email,
        })

def changeOptionEvent(request):
    if request.method == 'POST':
        event = EventModel.objects.filter(id=request.POST.get('idevent')).first()
        if request.POST.get('config_change') == "privacy":
            event.change_privacy()
        elif request.POST.get('config_change') == "showmap":
            event.change_showmap()
        elif request.POST.get('config_change') == "showtickets":
            event.change_tickets_remaining()

        return JsonResponse({'status':'OK'})
