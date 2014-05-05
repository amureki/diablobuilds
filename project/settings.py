# -*- coding:utf-8 -*-
import sys
import os
from configurations import Settings

from config.django.database import DevelopmentDatabaseSettings, StagingDatabaseSettings, ProductionDatabaseSettings, \
    TestDatabaseSettings
from config.django.i18n import LocaleSettings
from config.django.media import MediaSettings
from config.django.middleware import MiddlewareSetings
from config.django.logging import LoggingSettings
from config.django.template import TemplateSettings


class BaseSettings(LocaleSettings, MediaSettings, MiddlewareSetings, LoggingSettings, TemplateSettings, Settings):
    PROJECT_ROOT = os.path.realpath(os.path.dirname(__file__))
    sys.path.insert(0, os.path.join(PROJECT_ROOT, 'apps'))

    ADMINS = ()

    MANAGERS = ADMINS

    ALLOWED_HOSTS = []

    SITE_ID = 1

    SECRET_KEY = 'g-w$_bz2)*d=d$=1jr-v=3&xh%_9$#p06h@$37dft5so_-10!6'

    ROOT_URLCONF = 'project.urls'

    WSGI_APPLICATION = 'project.wsgi.application'

    INSTALLED_APPS = (
        'admin_tools',
        'admin_tools.theming',
        'admin_tools.menu',
        'admin_tools.dashboard',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'django.contrib.admin',
        'django.contrib.comments',

        'south',
        'gunicorn',
        'raven.contrib.django.raven_compat',
        'django'
    )


class Development(DevelopmentDatabaseSettings, BaseSettings):
    DEBUG = True
    TEMPLATE_DEBUG = DEBUG


class Staging(StagingDatabaseSettings, BaseSettings):
    RAVEN_CONFIG = {
        u'dsn': u'',
    }


class Production(ProductionDatabaseSettings, BaseSettings):
    RAVEN_CONFIG = {
        u'dsn': u'',
    }


class Jenkins(TestDatabaseSettings, BaseSettings):
    @property
    def INSTALLED_APPS(self):
        return BaseSettings.INSTALLED_APPS + ('django_jenkins',)

    JENKINS_TASKS = ('django_jenkins.tasks.run_pylint',
                     'django_jenkins.tasks.run_pep8',
                     'django_jenkins.tasks.run_pyflakes',
                     'django_jenkins.tasks.with_coverage',
                     'django_jenkins.tasks.django_tests',)

    PROJECT_APPS = ()