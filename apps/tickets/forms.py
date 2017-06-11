from django import forms
from apps.tickets.models import TicketModel,MethodsPaymentEventOffline

class TicketModelForm(forms.ModelForm):
    class Meta:
        model = TicketModel
        fields = [
            'title',
            'quantity',
            'price',
            'description',
            'start_sales_date',
            'start_sales_time',
            'end_sales_date',
            'end_sales_time',
            'number_tickets_order_min',
            'number_tickets_order_max',
            'visibility',
            'start_visibility_date',
            'start_visibility_time',
            'end_visibility_date',
            'end_visibility_time',
        ]

        labels = {
            'title' : 'Nombre del ticket',
            'quantity' : 'Cantidad de tickets',
            'price' : 'Precio del ticket',
            'description' : 'Descripcion del ticket',
            'start_sales_date' : 'Fecha Inicio de ventas',
            'start_sales_time' : 'Hora Inicio de ventas',
            'end_sales_date' : 'Fecha Fin de ventas',
            'end_sales_time' : 'Hora Fin de ventas',
            'number_tickets_order_min' : 'Minimo de tickets por compra',
            'number_tickets_order_max' : 'Maximo de tickets por compra',
            'visibility' : 'Quieres que el ticket sea visible?',
            'start_visibility_date' : 'Fecha para mostrar el ticket',
            'start_visibility_time' : 'Hora para mostrar el ticket',
            'end_visibility_date' : 'Fecha para dejar de mostrar el ticket',
            'end_visibility_time' : 'Hora para dejar de mostrar el ticket',
        }


        widgets = {
          'title' : forms.TextInput(attrs={'class':'form-control'}),
          'quantity' : forms.NumberInput(attrs={'class':'form-control','min':'0'}),
          'price' : forms.NumberInput(attrs={'class':'form-control','min':'0'}),
          'description' : forms.Textarea(attrs={'class':'form-control'}),
          'start_sales_date' : forms.TextInput(attrs={'class':'form-control form_date','placeholder':'Fecha de inicio de ventas', 'data-date':'', 'data-date-format':'dd/mm/yyyy', 'data-link-field':'dtp_input2'}),
          'start_sales_time' : forms.TextInput(attrs={'class':'form-control form_time','placeholder':'Hora de inicio de ventas', 'data-date':'', 'data-date-format':'hh:ii:ss', 'data-link-field':'dtp_input3'}),
          'end_sales_date' : forms.TextInput(attrs={'class':'form-control form_date','placeholder':'Fecha final de ventas', 'data-date':'', 'data-date-format':'dd/mm/yyyy', 'data-link-field':'dtp_input2'}),
          'end_sales_time' : forms.TextInput(attrs={'class':'form-control form_time','placeholder':'Hora final de ventas', 'data-date':'', 'data-date-format':'hh:ii:ss', 'data-link-field':'dtp_input3'}),
          'number_tickets_order_min' : forms.NumberInput(attrs={'class':'form-control','min':'0'}),
          'number_tickets_order_max' : forms.NumberInput(attrs={'class':'form-control','min':'1'}),
          'visibility' : forms.CheckboxInput(),
          'start_visibility_date' : forms.TextInput(attrs={'class':'form-control form_date','placeholder':'Fecha para ser visible', 'data-date':'', 'data-date-format':'dd/mm/yyyy', 'data-link-field':'dtp_input2'}),
          'start_visibility_time' : forms.TextInput(attrs={'class':'form-control form_time','placeholder':'Hora de inicio visibilidad', 'data-date':'', 'data-date-format':'hh:ii:ss', 'data-link-field':'dtp_input3'}),
          'end_visibility_date' : forms.TextInput(attrs={'class':'form-control form_date','placeholder':'Fin fecha para ser visible', 'data-date':'', 'data-date-format':'dd/mm/yyyy', 'data-link-field':'dtp_input2'}),
          'end_visibility_time' : forms.TextInput(attrs={'class':'form-control form_time','placeholder':'Hora fin de visibilidad', 'data-date':'', 'data-date-format':'hh:ii:ss', 'data-link-field':'dtp_input3'}),
        }


class MethodsPaymentEventOfflineForm(forms.ModelForm):
    class Meta:
        model = MethodsPaymentEventOffline
        fields = [
            'image',
            'title',
            'description',
            'message',
        ]

        labels = {
            'image' : "Logo",
            'title' : "Nombre del metodo",
            'description' : "Descripcion",
            'message' : "Mensaje de confirmacion",
        }

        widgets = {
            'image' : forms.FileInput(),
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'description' : forms.Textarea(attrs={'class':'form-control','rows':'4'}),
            'message' : forms.Textarea(attrs={'class':'form-control','rows':'4'}),
        }
