from django.shortcuts import render, redirect
import googletrans
from googletrans import Translator
from gtts import gTTS

# Create your views here.
def fnmake():
    from random import randint as ri
    st = ''

    for i in range(20):
        a = ri(1, 3)

        if a == 1:
            b = chr(ri(65, 90))

        elif a == 2:
            b = chr(ri(97, 122))

        else:
            b = ri(0, 9)

        b = str(b)
        st += b

    return st

def index(request):
    if request.user.is_anonymous:
        return redirect('acc:user_login')

    context = {
        'dic' : googletrans.LANGUAGES,
    }

    if request.method == 'POST':
        bf = request.POST.get('bf')
        lan = request.POST.get('lang')
        fname = fnmake()

        tts = gTTS(bf, lang=lan)
        tts.save(f'media/tts/{fname}.mp3')

        context.update({
            "bf": bf,
            "lang" : lan,
            'fn' : fname
        })

    return render(request, 'tts/index.html', context)

