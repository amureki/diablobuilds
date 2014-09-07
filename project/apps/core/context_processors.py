from core.models import News

def news(request):
    return {
        u'news': News.objects.all(),
    }