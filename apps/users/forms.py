from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.utils.timezone import now

from apps.users.models import UserInfoModel


class RegistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]

        labels = {
            'username': 'Nombre de Usuario',
            'first_name': 'Nombres',
            'last_name': 'Apellidos',
            'email': 'Correo',
            'password1' : 'Contraseña',
            'password2' : 'Repite la contraseña'
        }

        widgets = {
            'username' : forms.TextInput(attrs={'class':'form-control', 'required':'true'}),
            'first_name' : forms.TextInput(attrs={'class':'form-control', 'required' : 'true'}),
            'last_name' : forms.TextInput(attrs={'class':'form-control', 'required' : 'true'}),
            'email' : forms.TextInput(attrs={'class':'form-control', 'required' : 'true'}),
            'password1' : forms.PasswordInput(attrs={'class':'form-control', 'required':'true'}),
            'password2' : forms.PasswordInput(attrs={'class':'form-control', 'required':'true'}),
        }

class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfoModel
        fields = [
            'image_profile',
            'home_phone',
            'cell_phone',
            'job_title',
            'company',
            'website',
            'blog',
            'address',
            'address_two',
            'city',
            'country',
            'postal_code',
            'birth_date',
            'age',
            'preferences',
        ]

        labels = {
            'image_profile' : 'Foto de perfil',
            'home_phone' : 'Telefono Fijo',
            'cell_phone' : 'Numero Celular',
            'job_title' : 'Cargo',
            'company' : 'Empresa',
            'website' : 'Web',
            'blog' : 'Blog',
            'address' : 'Direccion',
            'address_two' : 'Direccion 2',
            'city' : 'Ciudad',
            'country' : 'Pais',
            'postal_code' : 'Codigo Postal',
            'birth_date' : 'Fecha Nacimiento',
            'age' : 'Edad',
            'preferences' : 'Preferencias',
        }

        widgets = {
          'image_profile' : forms.FileInput(),
          'home_phone' : forms.TextInput(attrs={'class':'form-control col-md-6'}),
          'cell_phone' : forms.TextInput(attrs={'class':'form-control col-md-6'}),
          'job_title' : forms.TextInput(attrs={'class':'form-control col-md-6'}),
          'company' : forms.TextInput(attrs={'class':'form-control col-md-6'}),
          'website' : forms.TextInput(attrs={'class':'form-control col-md-6'}),
          'blog' : forms.TextInput(attrs={'class':'form-control col-md-6'}),
          'address' : forms.TextInput(attrs={'class':'form-control col-md-6'}),
          'address_two' : forms.TextInput(attrs={'class':'form-control col-md-6'}),
          'city' : forms.TextInput(attrs={'class':'form-control col-md-6'}),
          'country' : forms.TextInput(attrs={'class':'form-control col-md-6'}),
          'postal_code' : forms.TextInput(attrs={'class':'form-control col-md-6'}),
          'birth_date' : forms.TextInput(attrs={'class':'form-control form_date', 'data-date':'', 'data-date-format':'dd/mm/yyyy', 'data-link-field':'dtp_input2'}),
          'age' : forms.NumberInput(attrs={'class':'form-control col-md-6'}),
          'preferences' : forms.CheckboxSelectMultiple(),
        }
