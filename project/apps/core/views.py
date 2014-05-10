# coding: utf-8
from django.core.urlresolvers import reverse
from django.views.generic import ListView, DetailView, CreateView, View
from rebranch_shortcuts.django.models import get_object_or_none
from rebranch_shortcuts.django.views import JSONResponseMixin
from project.apps.core.forms import CreateForm
from project.apps.core.models import Build, Guest


class IndexPage(ListView):
    template_name = u'index.html'
    model = Build
    context_object_name = u'builds'


class BuildsList(ListView):
    template_name = u'list.html'
    model = Build
    context_object_name = u'builds'


class BuildDetail(DetailView):
    template_name = u'detail.html'
    model = Build
    context_object_name = u'build'


class BuildChangeRating(View, JSONResponseMixin):
    def post(self, request, *args, **kwargs):
        action = request.POST.get(u'action', u'')
        build_id = request.POST.get(u'id', u'')

        ip = request.META.get('HTTP_X_FORWARDED_FOR', '') or request.META.get('REMOTE_ADDR', '')
        path = request.META.get('PATH_INFO')
        user_agent = request.META.get('USER_AGENT')
        referrer = request.META.get('HTTP_REFERRER')

        # if request.session.get(user_ip):
        #     rated = request.session.get(user_ip)
        #     if build_id in rated:
        #         data = {
        #             u'error': u'Вы уже голосовали за этот билд'
        #         }
        #         return self.render_to_json_response(status=self.response_status.fail, data=data)
        #     rated.append(build_id)
        #     request.session.modified = True
        # else:
        #     request.session[user_ip] = (build_id,)

        build = get_object_or_none(Build, id=build_id)

        guest, created = Guest.objects.get_or_create(
            ip=ip,
            defaults={
                u'user_agent': user_agent,
                u'referrer': referrer,
                u'path': path,
            }
        )
        if not created and build in guest.rated_builds.all():
            return self.render_to_json_response(
                status=self.response_status.fail,
                data={u'error': u'Вы уже голосовали за этот билд'}
            )

        guest.rated_builds.add(build)
        # guest.save()

        if not build or not action:
            return self.render_to_json_response(status=self.response_status.fail)

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
    template_name = u'create.html'
    form_class = CreateForm

    def get_success_url(self):
        return reverse(u'builds_list')