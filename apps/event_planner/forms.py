from django import forms
from apps.event_planner.models import EventPlannerModel,SponsorModel,GuestsModels,ShellersGroupModel,ShellerModel

class EventPlannerModelForm(forms.ModelForm):

    class Meta:
        model = EventPlannerModel
        fields = [
            'name',
            'image',
            'description',
            'twitter',
            'facebook',
        ]

        labels = {
            'name' : 'Nombre',
            'image' : 'Foto Organizador',
            'description' : 'Descripcion',
            'twitter' : 'Twitter',
            'facebook' : 'Facebook',
        }

        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'image' : forms.FileInput(),
            'description' : forms.Textarea(attrs={'class':'form-control'}),
            'twitter' : forms.TextInput(attrs={'class':'form-control'}),
            'facebook' : forms.TextInput(attrs={'class':'form-control'}),
        }

class SponsorModelForm(forms.ModelForm):
    class Meta:
        model = SponsorModel
        fields = [
            'title',
            'logo',
        ]

        labels = {
            'title' : 'Nombre del patrocinador',
            'logo' : 'Logo del patrocinador',
        }

        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'logo' : forms.FileInput(),
        }

class GuestModelForm(forms.ModelForm):
    class Meta:
        model = GuestsModels
        fields = [
            'name',
            'image',
            'twitter',
            'facebook',
        ]

        labels = {
            'name' : 'Nombre',
            'image' : 'Foto Invitado',
            'twitter' : 'Twitter',
            'facebook' : 'Facebook',
        }

        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'image' : forms.FileInput(),
            'twitter' : forms.TextInput(attrs={'class':'form-control'}),
            'facebook' : forms.TextInput(attrs={'class':'form-control'}),
        }

class ShellersGroupModelForm(forms.ModelForm):
    class Meta:
        model = ShellersGroupModel
        fields = [
            'title',
            'boss',
        ]

        labels = {
            'title' : 'Nombre del grupo',
            'boss' : 'Lider',
        }

        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'boss' : forms.Select(attrs={'class':'selectpicker','data-live-search':'true'}),
        }

class ShellerModelForm(forms.ModelForm):
    class Meta:
        model = ShellerModel
        fields = [
            'user',
        ]

        labels = {
            'user' : 'Vendedor',
        }

        widgets = {
            'user' : forms.Select(attrs={'class':'selectpicker','data-live-search':'true'}),
        }
