from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.hashers import check_password
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'acc/index.html')

def signup(request):
    if request.user.is_authenticated:
        return redirect('acc:index')

    if request.method == 'POST':
        pw = request.POST.get('password1')
        un = request.POST.get('username')
        up = request.FILES.get('userpic')
        uc = request.POST.get('comment')
        ua = request.POST.get('age')

        User.objects.create_user(username=un, password=pw, pic=up, comment=uc, age=ua)

        return redirect('acc:user_login')


    return render(request, 'acc/signup.html')

def user_login(request):
    if request.user.is_authenticated:
        return redirect('acc:index')

    if request.method == 'POST':
        un = request.POST.get('username')
        pw = request.POST.get('password')

        u = authenticate(username=un, password=pw)

        if u:
            login(request, u)
            messages.success(request, f'{u}님, 환영합니다!')
        else:
            messages.info(request, '계정 정보가 일치하지 않습니다')

        return redirect('acc:user_login')

    return render(request, 'acc/login.html')

def user_logout(request):
    if not request.user.is_authenticated:
        return redirect('acc:index')

    logout(request)
    return redirect('acc:index')

def profile(request):
    if not request.user.is_authenticated:
        return redirect('acc:index')

    return render(request, 'acc/profile.html')

def user_delete(request):
    if not request.user.is_authenticated:
        return redirect('acc:index')
    
    if request.method == 'POST':
        up = request.POST.get('password')
        upw = request.user.password

        if check_password(up, upw):
            u = request.user

            if u.pic:
                u.pic.delete()

            u.delete()
            return redirect('acc:index')
        
    return redirect('acc:index')

def update(request):
    if not request.user.is_authenticated:
        return redirect('acc:index')

    if request.method == 'POST':
        u = request.user

        u.pic.delete()

        up = request.FILES.get('userpic')
        ue = request.POST.get('email')
        uc = request.POST.get('comment')
        ua = request.POST.get('age')

        u.pic, u.comment, u.age, u.email = up, uc, ua, ue
        u.save()

        return redirect('acc:profile')

    return render(request, 'acc/update.html')

def chpass(request):
    if not request.user.is_authenticated:
        return redirect('acc:index')

    if request.method == 'POST':
        u = request.user
        old_pw = request.POST.get('cpw')
        qwe_pw = u.password
        up = request.POST.get('npw')

        if check_password(old_pw, qwe_pw):
            u.set_password(up)
            u.save()
            return redirect('acc:user_login')
        









