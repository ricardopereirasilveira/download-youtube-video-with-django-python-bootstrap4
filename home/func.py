from pytube import YouTube
import glob
import shutil
import os



# TODO reestruturar para usar Orientação ao Objeto;
def videoDownload(url):
    yt = YouTube(url)
    yt.streams.order_by('resolution')[-1].download()
    movingFileToCorrectPath(flag='video')
    yt.streams.filter(only_audio=True)[-1].download()
    movingFileToCorrectPath(flag='audio')
    joinFile()
    title = yt.title
    urlVideo = 'https://www.youtube.com/watch?v=' + yt.video_id
    views = yt.views
    thumbnail = yt.thumbnail_url
    author = yt.author
    renameLastFile(title=title)
    # print(title, urlVideo, views, thumbnail, author)


# TODO: Movendo arquivo para a pasta /static/video/
# FIXME: Criar folder 'video' caso não exista
def movingFileToCorrectPath(flag):
    if not os.path.exists('/static/video'):
        os.makedirs('static/video', exist_ok=True)

    try:
        if flag == 'video':
            for file in glob.glob('*.webm'):
                os.renames(file, f'video-{file}')
                a = f'video-{file}'
            shutil.move(a, 'static/video/')
        elif flag == 'audio':
            for file in glob.glob('*.webm'):
                os.renames(file, f'audio-{file}')
                a = f'audio-{file}'
            shutil.move(a, 'static/video/')
        return
    except Exception as e:
        print(e)


def joinFile():
    arquivos = []
    for file in glob.glob('static/video/*.webm'):
        arquivos.append(file)
    arquivo1 = arquivos[0]
    arquivo2 = arquivos[1]
    joinFile = f'ffmpeg -i "{arquivo1}" -i "{arquivo2}" -c:v copy -c:a aac static/video/videofull.mp4'
    os.system(joinFile)
    for file in glob.glob('static/video/*.webm'):
        os.remove(file)
    return

def renameLastFile(title):
    for x in glob.glob('static/video/*.mp4'):
        os.renames(x, f'media/{title.replace(" ", "")}.mp4')
