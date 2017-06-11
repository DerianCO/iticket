from django import forms
from apps.events.models import EventModel,TypeEventModel,TypeLocation, ImagesEvent, GalleryEvent, EventSchedule

class TypeEventForm(forms.ModelForm):
    class Meta:
        model = TypeEventModel
        fields = [
            'tile',
            'description',
        ]

        labels = {
            'tile' : 'Titulo',
            'description' : 'Descripcion',
        }

        widgets = {
            'tile' : forms.TextInput(attrs={'class':'form-control'}),
            'description' : forms.Textarea(attrs={'class':'form-control'}),
        }

class TypeLocationForm(forms.ModelForm):
    class Meta:
        model = TypeLocation
        fields = [
            'title',
            'description',
        ]

        labels = {
            'title': 'Titulo',
            'description': 'Descripcion',
        }

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }

class EventForm(forms.ModelForm):
    class Meta:
        model = EventModel
        fields = [
            'title',
            'location_type',
            'location_name',
            'location_address',
            'location_address_latitude',
            'location_address_longitude',
            'location_state',
            'location_country',
            'location_postal_code',
            'show_map',
            'start_date',
            'start_time',
            'end_date',
            'end_time',
            'description',
            'privacy',
            'show_tickets_remaining',
            'type_event',
        ]

        labels = {
            'title' : 'Titulo',
            'location_type' : 'Tipo de evento',
            'location_name' : 'Nombre del lugar',
            'location_address' : 'Direccion 1',
            'location_address_latitude': 'latitude',
            'location_address_longitude' : 'longitude',
            'location_state' : 'Estado',
            'location_country' : 'Pais',
            'location_postal_code' : 'Codigo Postal',
            'show_map' : 'Mostrar mapa en la pagina del evento?',
            'start_date' : 'Fecha de inicio del evento',
            'start_time' : 'Hora de inicio del evento',
            'end_date' : 'Fecha en que termina el evento',
            'end_time' : 'Hora en que termina el evento',
            'description' : 'Descripcion del evento',
            'privacy' : 'Evento privado?',
            'show_tickets_remaining' : 'Mostrar tikets restantes en la pagina?',
            'type_event' : 'Categoria del evento',
        }

        widgets =  {
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'location_type' : forms.Select(attrs={'class':'form-control'}),
            'location_name' : forms.TextInput(attrs={'class':'form-control'}),
            'location_address' : forms.TextInput(attrs={'class':'form-control'}),
            'location_address_latitude': forms.TextInput(attrs={'class':'form-control'}),
            'location_address_longitude': forms.TextInput(attrs={'class':'form-control'}),
            'location_state' : forms.TextInput(attrs={'class':'form-control'}),
            'location_country' : forms.TextInput(attrs={'class':'form-control'}),
            'location_postal_code' : forms.TextInput(attrs={'class':'form-control'}),
            'show_map' : forms.CheckboxInput(attrs={'class':'form-control'}),
            'start_date' : forms.TextInput(),
            'start_time' : forms.TimeInput(attrs={'class':'form-control'}),
            'end_date' : forms.TextInput(),
            'end_time' : forms.TimeInput(attrs={'class':'form-control'}),
            'description' : forms.Textarea(attrs={'class':'form-control'}),
            'privacy' : forms.CheckboxInput(attrs={'class':'form-control'}),
            'show_tickets_remaining' : forms.CheckboxInput(attrs={'class':'form-control'}),
            'type_event' : forms.Select(attrs={'class':'form-control'}),
        }


class ImagesEventForm(forms.ModelForm):
    class Meta:
        model = ImagesEvent
        fields = [
            'image',
        ]

        labels = {
            'image': 'Imagen del evento',
        }

        widgets = {
            'image' : forms.FileInput(),
        }

class GalleryEventForm(forms.ModelForm):
    class Meta:
        model = GalleryEvent
        fields = [
            'image',
        ]

        labels = {
            'image': 'Imagen del evento',
        }

        widgets = {
            'image' : forms.FileInput(),
        }

class EventScheduleForm(forms.ModelForm):
    class Meta:
        model = EventSchedule
        fields = [
            'title',
            'start_date',
            'start_time',
            'end_date',
            'end_time',
            'image',
        ]

        labels = {
            'title' : 'Titulo de la actividad',
            'start_date' : 'Fecha de inicio de la actividad',
            'start_time' : 'Hora inicio de la actividad',
            'end_date' : 'Fecha final de la actividad',
            'end_time' : 'Hora final de la actividad',
            'image' : 'Imagen de la actividad',
        }

        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'start_date': forms.TextInput(attrs={'class':'form-control form_date','placeholder':'Fecha inicio', 'data-date':'', 'data-date-format':'dd/mm/yyyy', 'data-link-field':'dtp_input2'}),
            'start_time': forms.TextInput(attrs={'class':'form-control form_time','placeholder':'Hora de inicio', 'data-date':'', 'data-date-format':'hh:ii:ss', 'data-link-field':'dtp_input3'}),
            'end_date': forms.TextInput(attrs={'class':'form-control form_date','placeholder':'Fecha Final', 'data-date':'', 'data-date-format':'dd/mm/yyyy', 'data-link-field':'dtp_input2'}),
            'end_time':forms.TextInput(attrs={'class':'form-control form_time','placeholder':'Hora final', 'data-date':'', 'data-date-format':'hh:ii:ss', 'data-link-field':'dtp_input3'}),
            'image' : forms.FileInput(),
        }
