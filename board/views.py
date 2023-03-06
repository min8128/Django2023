from django.shortcuts import render, redirect
from .models import Board, Reply
from django.core.paginator import Paginator
from django.contrib import messages


# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect('acc:user_login')
    
    page = request.GET.get('page', 1)
    cate = request.GET.get('cate', '')
    kw = request.GET.get('kw', '')

    if kw:
        if cate == 'title':
            b = Board.objects.filter(subject__startswith=kw)

        elif cate == 'writer':
            try:
                from acc.models import User
                u = User.objects.get(username=kw)
                b = Board.objects.filter(writer=u)
            except:
                b = Board.objects.none()

        elif cate == 'content':
            b = Board.objects.filter(content__contains=kw)
    
    else:
        b = Board.objects.all()
    
    b = b.order_by('-pubdate')

    pag = Paginator(b, 3)
    obj = pag.get_page(page)

    context = {
        'bset' : obj,
        'page' : page,
        'cate' : cate,
        'kw' : kw
    }
    return render(request, 'board/index.html', context)


def detail(request, bpk):
    if request.user.is_anonymous:
        return redirect('acc:user_login')
    
    b = Board.objects.get(id=bpk)
    c = b.reply_set.all()

    context = {
        'b' : b,
        'cset' : c
    }
    return render(request, 'board/detail.html', context)


def create(request):
    if request.user.is_anonymous:
        return redirect('acc:user_login')
    
    if request.method == 'POST':
        sb = request.POST.get('subject')
        cn = request.POST.get('content')
        u = request.user

        Board(subject=sb, content=cn, writer=u).save()
        return redirect('board:index')
    
    return render(request, 'board/create.html')


def update(request, bpk):
    if request.user.is_anonymous:
        return redirect('acc:user_login')
    
    
    
    b = Board.objects.get(id=bpk)

    if not b.writer == request.user:
        return redirect('board:detail', bpk)


    context = {
        'b' : b
    }

    if request.method == 'POST':
        sb = request.POST.get('subject')
        cn = request.POST.get('content')

        b.subject, b.content = sb, cn
        b.save()

        return redirect('board:detail', bpk)


    return render(request, 'board/update.html', context)

def delete_content(request, bpk):
    if request.user.is_anonymous:
        return redirect('acc:user_login')
    
    b = Board.objects.get(id=bpk)

    if request.user == b.writer:
        b.delete()

    else:
        messages.error(request, '비정상적인 접근이 확인되었습니다')

    return redirect('board:index')


def add_reply(request, bpk):
    if request.user.is_anonymous:
        return redirect('acc:user_login')
    
    com = request.GET.get('comment')
    b = Board.objects.get(id=bpk)

    Reply(board=b, replyer=request.user, comment=com).save()

    return redirect('board:detail', bpk)

def update_reply(request, bpk, rpk):
    if request.user.is_anonymous:
        return redirect('acc:user_login')
        

    com = request.GET.get('comment')
    r = Reply.objects.get(id=rpk)

    if request.user == r.replyer:
        r.comment = com
        r.save()

    return redirect('board:detail', bpk)

def delete_reply(request, bpk, rpk):
    if request.user.is_anonymous:
        return redirect('acc:user_login')
    
    r = Reply.objects.get(id=rpk)
    if request.user == r.replyer:
        r.delete()
    
    return redirect('board:detail', bpk)


def likey(request, bpk):
    if request.user.is_anonymous:
        return request('acc:user_login')
    
    b = Board.objects.get(id=bpk)

    if not request.user in b.likey.all():
        b.likey.add(request.user)

    return redirect('board:detail', bpk)

def unlikey(request, bpk):
    if request.user.is_anonymous:
        return request('acc:user_login')
    
    b = Board.objects.get(id=bpk)

    if request.user in b.likey.all():
        b.likey.remove(request.user)

    return redirect('board:detail', bpk)







