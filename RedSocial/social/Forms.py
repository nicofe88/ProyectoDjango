from django import forms
from django.forms import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.password_validation import validate_password
import re

def validate_name(value):
    if any(char.isdigit() for char in value):
        raise ValidationError('El nombre solo puede contener letras. %(valor)s',
                              code= 'Invalid',
                              params= {'valor': value})

def validate_email(value):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_regex, value):
        raise ValidationError('Correo inválido')
    return value


class UserRegister(forms.Form, UserCreationForm):

    user_name = forms.CharField(
        label= 'Nombre',
        max_length= 50,
        validators= (validate_name,),
        widget=forms.TextInput(attrs={'class': 'form-control',
                                        'placeholder':'Solo letras'}
                                )
    )
    user_email = forms.EmailField(
        label='Email',
        max_length= 100,
        required= True,
        validators= (validate_email,),
        error_messages= {
            'required':'Completa este campo'    
        },
        widget=forms.TextInput(attrs={'class': 'form-control', 
                                      'type': 'email'
                                })
    )
    password1 = forms.CharField(
        label= 'Password',
        widget= forms.PasswordInput
    )
    password2 = forms.CharField(
        label= 'Password confirmation',
        widget= forms.PasswordInput
    )

    def reset_password_confirmation(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 !=password2:
            raise forms.ValidationError(
                self.error_messages['different_passwords'],
                code='different_passwords'
            )
        validate_password(password1)
        return password2 
    
    # user_password = forms.PasswordInput(
    #     label ='Password',
    #     max_lenght= 20,
    #     requerid = True,
    #     validators= (validate_password,),
    #     error_messages= {
    #         'required': 'Completa este campo'
    #     },
    #     widget= forms.TextInput(attrs={'class':'form-control',
    #                                    'type':'password'
    #                             })
    # )