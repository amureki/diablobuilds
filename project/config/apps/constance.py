# encoding=utf8


class ConstanceBaseSettings(object):
    CONSTANCE_CONFIG = {
        'CURRENT_GAME_VERSION': (u'2.1.0', u'Текущая версия игры'),
    }


class ConstanceDevelopmentSettings(ConstanceBaseSettings):
    CONSTANCE_REDIS_CONNECTION = 'redis://localhost:6379/0'


class ConstanceStagingSettings(ConstanceBaseSettings):
    CONSTANCE_REDIS_CONNECTION = u'redis://diablobuilds-redis:6379/0'