from rebranch_deployment.docker.services.postgresql.proxy import PostgresqlService
from rebranch_deployment.docker.services.django.proxy import DjangoService
from rebranch_deployment.docker.processes.web.proxy import WebProcess
from rebranch_deployment.docker.process_managers.supervisor.proxy import SupervisorProcessManager
from rebranch_deployment.local.user_configuration import UserConfigurationFactoryAbstract


class BaseUserConfigurationFactory(UserConfigurationFactoryAbstract):
    def get_main_app(self):
        app = DjangoService(
            SupervisorProcessManager(
                startup_cmd=u'supervisord --nodaemon',
                processes=[
                    WebProcess(
                        name=u'main_web',
                        cmd=u'uwsgi --socket /etc/opa.sock --module project.wsgi --chmod-socket=666 --logto /app/log.log'
                    )
                ]
            )
        )

        postgresql = PostgresqlService()

        app.uses(postgresql)
        return app


class Staging(BaseUserConfigurationFactory):
    HOSTNAME = u'188.226.242.137'
    USERNAME = u'root'
    SERVER_NAMES = [u'diablobuilds.ru', ]
    APT_PACKAGES = []
    GIT_BRANCH = u'master'