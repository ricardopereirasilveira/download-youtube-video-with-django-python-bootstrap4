from django.shortcuts import render, redirect
from pytube import YouTube

from . import func


# TODO: Implementar o metodo que faça a conversão do vídeo
# TODO: Implementar um LOG de vídeos baixados para poder informar
#       na página posteriormente, com a função 'with open'
def index(request):
    """
    Here we load the index website to user insert the link of video to download.
    If the first visit, it dont access the IF.
    After user insert the link and click in submit, it goes inside the IF to download
        the video and the audio to convert then and give it to user download.
    :param request: receive the requisition get from input in HTML ( with link )
    :return: it return the request(without GET), return the page to load to user
            and return the video var
    """
    # 'https://www.youtube.com/watch?v = KTji1hOICEI'
    link = request.GET.get('link-youtube', None)
    video = None
    if link != None:
        yt = YouTube(link)
        video = func.videoConvert(yt)
        return render(request, 'result.html', {'video': video})
    return render(request, 'index.html', {'video': video})


# TODO: Aqui é a página que será redirecionada após receber a URL do passo anterior
# FIXME: Caso o usuário queira fazer o download de um vídeo daqui, ele não vai conseguir.
def result(request):
    return render(request, 'result.html')