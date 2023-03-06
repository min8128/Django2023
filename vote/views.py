from django.shortcuts import render, redirect
from .models import Topic, Choice
from django.contrib import messages

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect('acc:user_login')
    
    t = Topic.objects.all()

    context = {
        'tset' : t
    }

    return render(request, 'vote/index.html', context)

def detail(request, vpk):
    if request.user.is_anonymous:
        return redirect('acc:user_login')
    
    t = Topic.objects.get(id=vpk)
    c = t.choice_set.all()

    context = {
        't' : t,
        'cset' : c
    }
    

    return render(request, 'vote/detail.html', context)

def create(request):
    if request.user.is_anonymous:
        return redirect('acc:user_login')
    
    if request.method == 'POST':
        nm = request.POST.get('title')
        con = request.POST.get('det')
        pic = request.FILES.get('pic')
        cn = request.POST.getlist('con')
        cc = request.POST.getlist('com')

        t = Topic(title=nm, maker=request.user, content=con, pic=pic)
        t.save()

        for i, j in zip(cn, cc):
            Choice(top=t, name=i, comment=j).save()

        return redirect('vote:index')

    return render(request, 'vote/create.html')

def vote(request, vpk): 
    if request.user.is_anonymous:
        return redirect('acc:user_login')
    
    t = Topic.objects.get(id=vpk)

    if not request.user in t.voter.all():
        t.voter.add(request.user)
        cpk = request.POST.get('cho')
        c = Choice.objects.get(id=cpk)
        c.choicer.add(request.user)
        c.save()
    
    return redirect('vote:detail', vpk)

def delete(request, vpk):
    if request.user.is_anonymous:
        return redirect('acc:user_login')
    
    t = Topic.objects.get(id=vpk)

    if request.user == t.maker:
        t.pic.delete()
        t.delete()
    else:
        messages.error(request, '이거 니꺼 아니니깐 지우지 마세요')
    
    return redirect('vote:index')

def cancel(request, vpk):
    if request.user.is_anonymous:
        return redirect('acc:user_login')
    
    t = Topic.objects.get(id=vpk)
    u = request.user
    t.voter.remove(u)
    u.choice_set.get(top=t).choicer.remove(u)

        
    
    return redirect('vote:detail', vpk)







