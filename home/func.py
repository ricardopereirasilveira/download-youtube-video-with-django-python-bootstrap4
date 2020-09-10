from pytube import YouTube
import shutil


# TODO: Aqui estamos baixando o vídeo e enviando o caminho de volta
#       DUVIDA: Como excluir o vídeo após enviar ao usuário para não
#       sobrecarregar o servidor?
# TODO: VIDEO = é o caminho do vídeo para download
# TODO: URL = é a URL do vídeo, para obter informações para a página.
def videoConvert(infoVideo):
    # video = infoVideo.streams.order_by('resolution')[-1].download()
    audio = infoVideo.streams.filter(only_audio=True)[-1].download()
    title = infoVideo.title
    urlVideo = 'https://www.youtube.com/watch?v=' + infoVideo.video_id
    views = infoVideo.views
    thumbnail = infoVideo.thumbnail_url
    author = infoVideo.author
    print(f'{title} \n {urlVideo} \n {views} \n {thumbnail} \n {author}')

    location = arquivo()
    url = None
    return (url)


# TODO: Irá receber a informação do vídeo para ser inserida no results
#       como últimos vídeos baixados.
def infoVideo(url):
    pass


# TODO: Aqui iremos jogar o vídeo para a pasta STATIC e devolver o
#       caminho do arquivo, para ser inserido na tag A do HTML.
def arquivo():
    pass