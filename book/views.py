from django.shortcuts import render, redirect
from .models import Books
from django.contrib import messages

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect('acc:user_login')
    
    b = request.user.books_set.all()

    context = {
        'bset' : b
    }
    
    return render(request, 'book/index.html', context)
    

def create(request):
    if request.user.is_anonymous:
        return redirect('acc:user_login')
    
    if request.method == 'POST':
        nm = request.POST.get('nm')
        url = request.POST.get('url')
        con = request.POST.get('con')
        imp = request.POST.get('ip')
        
        if imp == 'on':
            imp = True
        else:
            imp = False

        Books(user=request.user, site_name=nm, site_url=url, site_con=con, impo=imp).save()

        return redirect('book:index')

    return render(request, 'book/create.html')

def delete(request, bpk):
    if request.user.is_anonymous:
        return redirect('acc:user_login')
    
    b = Books.objects.get(id=bpk)

    if b.user == request.user:
        b.delete()
    else:
        messages.warning(request, '비정상적인 접근이 확인되었습니다')
    
    return redirect('book:index')