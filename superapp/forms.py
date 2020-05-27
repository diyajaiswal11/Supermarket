from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from django.contrib.auth import authenticate, get_user_model
from .models import Product, Customer

#from django.contrib.auth.models import User

#User=get_user_model()

class ProductForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Name'}))
    company = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Company'}))
    protype = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Type'}))
    cost = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Cost'}))
    class Meta:
        model=Product
        fields=['name','company','protype','cost']


class CustomerForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Name'}))
    phoneno = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Phone Number'}))
    class Meta:
        model=Customer
        fields=['name','phoneno'] 



class OrderForm(forms.ModelForm):
    class Meta:
        model=Customer 
        fields=['products']








class CreateUserForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password','class':'input100'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password', 'class':'input100'}))
    class Meta:
        model = User
        fields=['username','email','password1','password2']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder':'Username', 'class':'input100'}),
            'email': forms.TextInput(attrs={'placeholder':'Email', 'class':'input100'}),
        }
        
class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username','class':'input100'}),)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password','class':'input100'}))
    def clean(self, *args, **kwargs):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('Invalid Username or Password')
            if not user.check_password(password):
                raise forms.ValidationError('Wrong Password')
            if not user.is_active:
                raise forms.ValidationError('not active')
        return super(UserLoginForm, self).clean(*args, **kwargs) 