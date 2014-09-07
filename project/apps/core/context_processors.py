from core.models import News, Build


def news(request):
    return {
        u'news': News.objects.all(),
    }


def builds_count(request):
    return {
        u'barbarian_builds_count': Build.objects.filter(hero_class=0).count(),
        u'crusader_builds_count': Build.objects.filter(hero_class=1).count(),
        u'demonhunter_builds_count': Build.objects.filter(hero_class=2).count(),
        u'monk_builds_count': Build.objects.filter(hero_class=3).count(),
        u'witchdoctor_builds_count': Build.objects.filter(hero_class=4).count(),
        u'wizard_builds_count': Build.objects.filter(hero_class=5).count(),
    }