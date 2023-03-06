from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect('acc:user_login')
    
    t = request.user.todo_set.all()

    context = {
        'tset' : t
    }
     
    return render(request, 'todo/index.html', context)

def create(request):
    u = request.user

    if u.is_anonymous:
        return redirect('acc:user_login')
    
    nm = request.POST.get('name')

    Todo(user=u, name=nm).save()
     
    return redirect('todo:index')

def finish(request, tpk):
    u = request.user

    if u.is_anonymous:
        return redirect('acc:user_login')
    
    t = Todo.objects.get(id=tpk)

    if request.user == t.user:
        t.done = True
        t.save()
    
    return redirect('todo:index')

def delete(request, tpk):
    u = request.user

    if u.is_anonymous:
        return redirect('acc:user_login')
    
    t = Todo.objects.get(id=tpk)

    if request.user == t.user:
        t.delete()
    
    return redirect('todo:index')