# coding: utf-8
from datetime import datetime
from django.contrib import messages
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, View, TemplateView
from rebranch_shortcuts.django.models import get_object_or_none
from rebranch_shortcuts.django.views import JSONResponseMixin
from project.apps.core.forms import CreateForm
from project.apps.core.models import Build, Guest, Vote


class IndexPage(ListView):
    template_name = u'index.html'
    model = Build
    context_object_name = u'builds'

    def get_queryset(self):
        return self.model.published_objects.all()


class BuildsList(ListView):
    template_name = u'list.html'
    model = Build
    context_object_name = u'builds'

    HERO_CLASSES = {
        u'barbarian': 0,
        u'crusader': 1,
        u'demon-hunter': 2,
        u'monk': 3,
        u'witch-doctor': 4,
        u'wizard': 5,
    }

    SORT_PARAMS = (u'date_created', u'rating')

    def __init__(self, **kwargs):
        super(BuildsList, self).__init__(**kwargs)
        self.query = {}

    def get_queryset(self):
        sort = self.request.GET.get(u'sort', None)
        hero_class = self.kwargs.get(u'optional', None)
        if hero_class and hero_class in self.HERO_CLASSES.keys():
            self.query[u'hero_class'] = self.HERO_CLASSES[hero_class]
        builds = self.model.published_objects.filter(**self.query)
        if sort and sort in self.SORT_PARAMS:
            builds = reversed(builds.order_by(sort))
        return builds


class BuildDetail(DetailView):
    template_name = u'detail.html'
    model = Build
    context_object_name = u'build'


class BuildVote(View, JSONResponseMixin):
    def post(self, request, *args, **kwargs):
        action = request.POST.get(u'action', u'')
        build_id = request.POST.get(u'id', u'')

        ip = request.META.get('HTTP_X_FORWARDED_FOR', '') or request.META.get('REMOTE_ADDR', '')
        path = request.META.get('PATH_INFO')
        user_agent = request.META.get('USER_AGENT')
        referrer = request.META.get('HTTP_REFERRER')

        build = get_object_or_none(Build, id=build_id)

        if not build or not action:
            return self.render_to_json_response(status=self.response_status.fail)

        guest, _ = Guest.objects.get_or_create(
            ip=ip,
            defaults={
                u'user_agent': user_agent,
                u'referrer': referrer,
                u'path': path,
            }
        )

        vote, created = Vote.objects.get_or_create(
            date_voted=datetime.now(),
            build=build,
            guest=guest,
        )

        if not created:
            return self.render_to_json_response(
                status=self.response_status.fail,
                data={u'error': u'Вы уже голосовали за этот билд сегодня.'}
            )

        if action == u'up':
            build.rate_up()
        elif action == u'down':
            build.rate_down()
        else:
            return self.render_to_json_response(status=self.response_status.fail)

        data = {
            u'rating': build.rating
        }
        return self.render_to_json_response(status=self.response_status.success, data=data)


class BuildAdd(CreateView):
    template_name = u'add.html'
    form_class = CreateForm

    def get_success_url(self):
        return reverse(u'index')

    def form_valid(self, form):
        messages.success(self.request, u'Билд успешно добавлен на модерацию.')
        build = form.cleaned_data.get(u'name', None)
        send_mail(
            u'Новый билд',
            u'На сайте появился новый билд под названием %s' % build,
            u'mail@diablobuilds.ru', [u'fly.amureki@gmail.com']
        )
        return HttpResponseRedirect(self.get_success_url())


class FAQPage(TemplateView):
    template_name = u'faq.html'