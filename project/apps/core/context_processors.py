from django.conf import settings


def current_game_version(request):
    return {u'CURRENT_GAME_VERSION': settings.CURRENT_GAME_VERSION}