from django import template
import glob

register = template.Library()


# TODO: Enviando arquivo para o template para download
@register.simple_tag
def sendingFileToTemplate():
    arquivo = None
    for file in glob.glob('static/video/*.mp4'):
       arquivo = file
    return arquivo