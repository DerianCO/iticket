from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from apps.events.views import EventView,CreateEvent,DashboardEvent,EventImages,EventTicket,PublishEvent,EventPlanner,EventSponsor,EventGuest,Delete,EventGallery,EventSchedules,getEvents,GetStatsTickets,TicketsSold,ReqAssistance,toAccept,EventShellers,addShellerInTheGroup,destroyEvent,EventConfigurations,changeOptionEvent,EventMethodsPaymentEventOffline,configPlatformPayment

urlpatterns = [
    url(r'^new$', login_required(CreateEvent), name='new'),
    url(r'^view/(?P<view>\w+)/(?P<idevent>\d+)/$', EventView, name='event_view_home'), #Basada en funciones
    url(r'^dashboard/(?P<idevent>\d+)/$', login_required(DashboardEvent), name='dashboard'), #Basada en funciones
    url(r'^dashboard/images/(?P<idevent>\d+)/$', login_required(EventImages), name='event_images'),  # Basada en funciones
    url(r'^dashboard/gallery/(?P<idevent>\d+)/$', login_required(EventGallery), name='event_gallery'),  # Basada en funciones
    url(r'^dashboard/tickets/(?P<idevent>\d+)/$', login_required(EventTicket), name='event_tickets'),# Basada en funciones
    url(r'^dashboard/publish/(?P<idevent>\d+)/$', login_required(PublishEvent), name='publish'),# Basada en funciones
    url(r'^dashboard/planners/(?P<idevent>\d+)/$', login_required(EventPlanner), name='event_planners'),# Basada en funciones
    url(r'^dashboard/sponsors/(?P<idevent>\d+)/$', login_required(EventSponsor), name='event_sponsors'),# Basada en funciones
    url(r'^dashboard/guests/(?P<idevent>\d+)/$', login_required(EventGuest), name='event_guests'),# Basada en funciones
    url(r'^dashboard/schedules/(?P<idevent>\d+)/$', login_required(EventSchedules), name='event_schedules'),# Basada en funciones
    url(r'^dashboard/shellers/(?P<idevent>\d+)/$', login_required(EventShellers), name='event_shellers'),# Basada en funciones
    url(r'^dashboard/configurations/(?P<idevent>\d+)/$', login_required(EventConfigurations), name='event_configurations'),# Basada en funciones
    url(r'^dashboard/paymentoffline/(?P<idevent>\d+)/$', login_required(EventMethodsPaymentEventOffline), name='paymentoffline'),# Basada en funciones
    url(r'^dashboard/delete/(?P<idevent>\d+)/$', login_required(Delete), name='event_delete'),
    url(r'^search/$', login_required(getEvents), name='getEvents'),
    url(r'^stats/tickets/$', login_required(GetStatsTickets), name='statsTickets'),
    url(r'^sold/tickets/$', login_required(TicketsSold), name='ticketsSold'),
    url(r'^requestassistance/$', login_required(ReqAssistance), name='reqassistance'),
    url(r'^toaccept/$', login_required(toAccept), name='toaccept'),
    url(r'^addsheller/$', login_required(addShellerInTheGroup), name='addsheller'),
    url(r'^destroy/$', login_required(destroyEvent), name='destroy'),
    url(r'^change_option/$', login_required(changeOptionEvent), name='changeOption'),
    url(r'^platformpayment/$', login_required(configPlatformPayment), name='platformpayment'),
]
