from jetee.service.services.primary import PrimaryService
from jetee.service.services.postgresql import PostgreSQLService
from jetee.service.services.redis import RedisService

from jetee.project.projects import DjangoProject
from jetee.common.user_configuration import AppConfiguration
from jetee.processes import UWSGIProcess


class Staging(AppConfiguration):
    hostname = u'128.199.47.187'
    username = u'root'
    server_names = [u'diablobuilds.ru']

    def get_primary_service(self):
        app_service = PrimaryService(
            project=DjangoProject(
                cvs_repo_url=u'git@bitbucket.org:amureki/diablobuilds.git',
                processes=[UWSGIProcess(u'project/wsgi.py')]
            )
        )
        return app_service

    def get_secondary_services(self):
        return [PostgreSQLService(), RedisService()]