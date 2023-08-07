from django.shortcuts import render, redirect
from .forms import RegisterForm , LoginForm
from django.contrib import messages
from django.contrib.auth import login , authenticate , logout
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect


@csrf_protect
def register(request):
    
    if request.user.is_authenticated :
            messages.info(request, 'zaten girdin la')
            return redirect('/')
    form = RegisterForm(request.POST or None)

    if form.is_valid():
        username =  form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')


        newUser = User( username = username)
        newUser.set_password(password)

        newUser.save()
        login(request, newUser)
        messages.info(request, 'Aferin lan kaydoldun')

        return redirect('/')
    
    context = {
        'form' : form
    }
    
    return render(request, 'arayuz/register.html', context)

@csrf_protect
def loginUser(request):

    if request.user.is_authenticated :
            messages.info(request, 'zaten girdin la')
            return redirect('/')
    form = LoginForm(request.POST or None)

    context = {
        'form' : form
    }
    
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username = username,password = password)

        

        if user is None:
            messages.info(request,'La yok la')
            return render(request, 'arayuz/login.html',context)
        
        
        
        messages.success(request, 'Aferin laaa')
        login(request, user)
        return redirect('/')
        
        
    return render(request, 'arayuz/login.html', context)
    
    
@csrf_protect
def logoutUser(request):
    logout(request)
    messages.success(request,"gittin ha")
    return redirect('/')
