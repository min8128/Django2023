from django.shortcuts import render, redirect
import googletrans
from googletrans import Translator

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect('acc:user_login')
    
    dic = googletrans.LANGUAGES

    fr = request.GET.get('from', 'en')
    to = request.GET.get('to', 'ko')

    ini = request.GET.get('initial', '')
    fin = request.GET.get('final', '')

    translator = Translator()

    if fr == 'detect':
        fr = translator.detect(ini).lang

    if ini:
        fin = translator.translate(ini, src=fr, dest=to).text

    context = {
        'dic' : dic,
        'fr' : fr,
        'to' : to,
        'ini' : ini,
        'fin' : fin
    }

    return render(request, 'trans/index.html', context)

def change(request):
    if request.user.is_anonymous:
        return redirect('acc:user_login')
    
    
    dic = googletrans.LANGUAGES

    fr = request.GET.get('from')
    to = request.GET.get('to')

    ini = request.GET.get('initial')

    translator = Translator()
    fin = translator.translate(ini, src=fr, dest=to).text

    context = {
        'dic' : dic,
        'fr' : to,
        'to' : fr,
        'ini' : fin,
        'fin' : ini
    }

    return render(request, 'trans/index.html', context)
