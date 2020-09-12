from pytube import YouTube


def videoDownload(url):
    yt = YouTube(url)
    titulo = yt.title
    video = yt.streams.filter(re)