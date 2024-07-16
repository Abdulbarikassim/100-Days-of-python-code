from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django import forms 
from .models import Record

from django.forms.widgets import PasswordInput,TextInput


#  create/register a user. 
class CreateUser(UserCreationForm):
    class Meta: 
        model = User

        fields = ['username','password1','password2']
# login 

class LoginUser(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())


#  Create records 

class CreateRecord(forms.ModelForm):

    class Meta:

        model = Record
        fields =['first_name','last_name','email','phone','address','city','province','country']

#  Update records 

class UpdateRecord(forms.ModelForm):

    class Meta:

        model = Record
        fields =['first_name','last_name','email','phone','address','city','province','country']
