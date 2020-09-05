from pytube import YouTube


# TODO: Aqui estamos baixando o vídeo e enviando o caminho de volta
#       DUVIDA: Como excluir o vídeo após enviar ao usuário para não
#       sobrecarregar o servidor?
def videoConvert(url):
    # url = url.download()
    file = arquivo()
    # url = None
    print(url)
    return url

# TODO: Irá receber a informação do vídeo para ser inserida no results
#       como últimos vídeos baixados.
def infoVideo(url):
    pass

# TODO: Aqui iremos jogar o vídeo para a pasta STATIC e devolver o
#       caminho do arquivo, para ser inserido na tag A do HTML.
def arquivo():
    pass