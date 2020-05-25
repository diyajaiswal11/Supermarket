from django.shortcuts import render
from django.shortcuts import render
# Create your views here.
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from .forms import CreateUserForm, UserLoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login , logout, get_user_model
from django.http import HttpResponseBadRequest, JsonResponse
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
# Create your views here.
from .forms import ProductForm
from .models import Product


def viewproduct(request):
    products=Product.objects.all()
    return render(request,'viewproduct.html',{'products':products})




def editproduct(request,pk):
    item=get_object_or_404(Product,pk=pk)

    if request.method=='POST':
        form=ProductForm(request.POST,instance=item)
        if form.is_valid():
            form.save() 
            return redirect('viewproduct')

    else:
        form=ProductForm(instance=item) 
    
    return render(request,'editproduct.html',{'form':form})





def deleteproduct(request,pk):
    Product.objects.filter(id=pk).delete() 

    products=Product.objects.all()
    return render(request,'viewproduct.html',{'products':products})









def addproduct(request):
    if request.method=='POST':
        form=ProductForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('frontpage') 

    else:
        form=ProductForm()
    return render(request,'addproduct.html',{'form':form})


def logoutpage(request):
    logout(request)
    return redirect('home')

def home(request):
    return render(request,'home.html')


@login_required
def frontpage(request):
    return render(request,'frontpage.html')
    













def register(request):
    user=request.user
    if user.is_authenticated:
        return redirect('home') 
    else:
        if request.method == 'POST':
            form=CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user=form.cleaned_data.get('username')
                messages.success(request,'Account was created for '+ user)
                return redirect('loginpage')
        else:
            form=CreateUserForm()    
        context = {'form':form }    
        return render(request,'register.html',context)

def loginpage(request):
    user = request.user
    if user.is_authenticated:
        return redirect('frontpage') 
    else:
        next = request.GET.get('next')
        form = UserLoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            
            login(request, user)
            if next:
                return redirect(next)
            return redirect('frontpage')
        
        context = {
            'form': form,
        }
        return render(request, 'login.html', context)



