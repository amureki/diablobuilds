# -*- coding:utf-8 -*-
import sys
import os
from configurations import Settings

from config.django.database import DevelopmentDatabaseSettings, StagingDatabaseSettings
from config.django.i18n import LocaleSettings
from config.django.media import MediaSettings, ProductionMediaSettings
from config.django.middleware import MiddlewareSetings
from config.django.logging import LoggingSettings
from config.django.template import TemplateSettings
from config.django.email import EmailSettings

from config.apps.constance import ConstanceDevelopmentSettings, ConstanceStagingSettings
from config.apps.ckeditor import CKEditorSettings
from config.apps.disqus import DisqusSettings


class BaseSettings(LocaleSettings, MediaSettings, MiddlewareSetings, LoggingSettings, EmailSettings, TemplateSettings,
                   Settings, CKEditorSettings, DisqusSettings):
    PROJECT_ROOT = os.path.realpath(os.path.dirname(__file__))
    sys.path.insert(0, os.path.join(PROJECT_ROOT, 'apps'))

    ADMINS = MANAGERS = (
        ('amureki', 'fly.amureki@gmail.com'),
    )

    ALLOWED_HOSTS = [u'diablobuilds.ru', ]
    INTERNAL_IPS = ['127.0.0.1', ]

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
        'disqus',
        'ckeditor',
        'django',
        'constance',

        'core',
    )


class Development(DevelopmentDatabaseSettings, BaseSettings, ConstanceDevelopmentSettings):
    DEBUG = True
    TEMPLATE_DEBUG = DEBUG


class Staging(StagingDatabaseSettings, ProductionMediaSettings, ConstanceStagingSettings, BaseSettings):
    RAVEN_CONFIG = {
        u'dsn': u'',
    }