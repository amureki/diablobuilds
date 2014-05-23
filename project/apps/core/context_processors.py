from django.conf import settings
from core.models import News


def current_game_version(request):
    return { u'CURRENT_GAME_VERSION': settings.CURRENT_GAME_VERSION }


def news(request):
    return {
        u'news': News.objects.all(),
    }