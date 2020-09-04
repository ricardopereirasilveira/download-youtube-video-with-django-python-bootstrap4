from django.shortcuts import render, redirect
from pytube import YouTube

from . import func


# TODO: Implementar o metodo que faça a conversão do vídeo
def index(request):
    # 'https://www.youtube.com/watch?v = KTji1hOICEI'
    link = request.GET.get('link-youtube', None)
    video = None
    if link != None:
        yt = YouTube(link)
        video = yt.streams.order_by('resolution')[-1]
        video = func.videoConvert(video)
        return redirect('result')
    return render(request, 'index.html', {'video': video})


# TODO: Aqui é a página que será redirecionada após receber a URL do passo anterior
def result(request):
    return render(request, 'result.html')