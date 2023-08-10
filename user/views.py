from django.contrib import messages
from django.contrib.auth import login , authenticate , logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from .forms import RegisterForm , LoginForm

@csrf_protect
def register(request):
    
    if request.user.is_authenticated :
            messages.info(request, 'Zaten bir hesapla giriş yaptın!')
            return redirect('/')
    form = RegisterForm(request.POST or None)

    if form.is_valid():
        username =  form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')


        newUser = User(username = username)
        if User.objects.filter(username = username).first():
            messages.info(request, "Bu kullanıcı adı daha önce alındı")
            return redirect('user:register')
    
        newUser.set_password(password)

        newUser.save()
        login(request, newUser)
        messages.info(request, 'Bravo kaydoldun!')
        return redirect('/')
    
    
    
    context = {
        'form' : form
    }
    
    return render(request, 'interface/register.html', context)

@csrf_protect
def login_view(request):

    if request.user.is_authenticated :
            messages.info(request, 'Zaten girdin')
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
            messages.info(request,'Kullanici ismi veya parola yanlis')
            return render(request, 'interface/login.html',context)
        
        messages.success(request, 'Aferin giris yaptin')
        login(request, user)
        return redirect('/')
       
    return render(request, 'interface/login.html', context)
    
    
@csrf_protect
def logout_view(request):
    logout(request)
    messages.success(request,"Çıkış Yapıldı")
    return redirect('/')
