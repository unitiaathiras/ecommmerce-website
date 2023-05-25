from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def log(request):
    if request.method == 'POST':
        name = request.POST['name1']
        pswd = request.POST['pswd1']
        client = auth.authenticate(username=name, password=pswd)
        if client is not None:
            auth.login(request, client)
            return redirect('/')
        else:
            messages.info(request, "invalid credentials")
            return redirect('login')
    return render(request, "login.html")


def reg(request):
    if request.method == 'POST':
        name = request.POST['username']
        first = request.POST['first_name']
        second = request.POST['second_name']
        email = request.POST['email']
        pswd = request.POST['password1']
        pswd1 = request.POST['password2']
        if pswd == pswd1:
            if User.objects.filter(username=name).exists():
                messages.info(request, "username already exists")
                return redirect('registration')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email already exists")
                return redirect('registration')
            else:
                client = User.objects.create_user(username=name, first_name=first, last_name=second, email=email,
                                                  password=pswd)
                client.save()
                return redirect('login')
        else:
            messages.info(request, "password not matching")
            return redirect('registration')
        return redirect('/')
    return render(request, "register.html")


def out(request):
    auth.logout(request)
    return redirect('/')
