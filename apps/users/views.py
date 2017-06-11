from django.contrib.auth.models import User
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView

from apps.events.models import EventModel, ImagesEvent, TypeEventModel
from apps.tickets.models import TicketModel,PaymentMethod
from apps.users.forms import RegistroForm, UserInfoForm
from apps.users.models import UserInfoModel
from apps.configplatform.models import ConfigPlatform
from apps.event_planner.models import ShellersGroupModel,ShellerModel

def Profile(request,username):
    if request.method == 'GET':
        config = ConfigPlatform.objects.get(id=1)
        type_events = TypeEventModel.objects.all()
        if (request.user == User.objects.filter(username=username).first()):
            username = username
        else:
            username = request.user.username

        user = User.objects.filter(username=username).first()
        eventslist = EventModel.objects.filter(user=user)
        userinfo = UserInfoModel.objects.filter(user=user).first()

        if (UserInfoModel.objects.filter(user=user).exists()):
            form = UserInfoForm(instance=userinfo)
        else:
            form = UserInfoForm()

        events = []
        for event in eventslist:
            image = ImagesEvent.objects.filter(event=event).first()
            ticket = TicketModel.objects.filter(event=event).order_by('price').first()

            events.append({
                'event':event,
                'image':image,
                'ticket' : ticket,
            })

        group_sheller = []
        shellers = ShellerModel.objects.filter(user=request.user)
        for sheller in shellers:
            group = ShellersGroupModel.objects.get(id=sheller.group.id)

            group_sheller.append({
                'group' : group,
                'sheller' : sheller,
            })

        users = User.objects.all()
        methods = PaymentMethod.objects.all()


        context = {
            'user':user,
            'data_events':events,
            'userinfo':userinfo,
            'form':form,
            'config':config,
            'type_events':type_events,
            'group_sheller':group_sheller,
            'users' : users,
            'methods' : methods,
        }

        return render(request,'user/profile_home.html',context)

    elif request.method == 'POST':

        userinfo = UserInfoModel.objects.filter(user__username=username).first()
        if(UserInfoModel.objects.filter(user__username=username).exists()):
            form = UserInfoForm(request.POST, instance=userinfo)
            if form.is_valid():
                userinfo2 = form.save(commit=False)
                userinfo2.user = User.objects.filter(username=username).first()
                form.save()
        else:
            form = UserInfoForm(request.POST,request.FILES)
            if form.is_valid():
                userinfo = form.save(commit=False)
                userinfo.user = User.objects.filter(username=username).first()
                form.save()
        return redirect('profile:home',username)


def UserRegister(request):
    if request.method == 'GET':
        form = RegistroForm
        config = ConfigPlatform.objects.get(id=1)
        return render(request,'user/register.html',context={'form':form,'config':config})
    elif request.method == 'POST':
        register = RegistroForm(request.POST)
        
        if register.is_valid():
            register.save()

        return redirect('home')

class CreateProfile(CreateView):
    model = UserInfoModel
    template_name = 'user/profile_home.html'
    form_class = UserInfoForm
    success_url = reverse_lazy('home')
