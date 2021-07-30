from django import template

register = template.Library()


@register.filter()
def resaltar_texto(value):
    print("ola tudo bem")
    print(value)
    return 'deu certo'

@register.filter()
def extensao(value):
    # retorna a extensao:
    return value[-4:]


@register.filter()
def class_da_extensao(value):
    # retorna a class dependendo da extensao:
    ext = value[-4:]
    if ext in ['.jpg', '.png']:
        return 'img-thumbnail'
    elif ext in ['.mp4', '.avi']:
        return 'video-thumbnail'