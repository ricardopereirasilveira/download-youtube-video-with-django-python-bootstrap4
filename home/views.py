from django.shortcuts import render, redirect
from pytube import YouTube


# TODO: Implementar o metodo que faça a conversão do vídeo
def index(request):
    # 'https://www.youtube.com/watch?v = KTji1hOICEI'
    link = request.GET.get('link-youtube', None)
    if link != None:
        yt = YouTube(link)
        video = yt.streams.order_by('resolution')[-1]
        print(video)
    return render(request, 'index.html')


# TODO: Aqui é a página que será redirecionada após receber a URL do passo anterior
def result(request):
    return render(request, 'result.html')


# TODO: Aqui é onde a conversão vai acontecer, será que é melhor criar em outro .py ?
def videoConvert(url):
    pass