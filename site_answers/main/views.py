from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
import json

flag = False
def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                return render(request, 'main/register.html', {'error': 'Имя пользователя уже занято.'})
            else:
                user = User.objects.create_user(username=username, password=password1)
                user.save()
                return redirect('login')
        else:
            return render(request, 'main/register.html', {'error': 'Пароли не совпадают'})
    else:
        return render(request, 'main/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)

            data = {
                f"{user}":{}
            }
            with open('site_answers/main/static/main/js/answers.json', 'a') as f:
                json.dump(data, f)

            return redirect('news')
        else:
            return render(request, 'main/login.html', {'error': 'Введены неверные данные!'})
    else:
        return render(request, 'main/login.html')