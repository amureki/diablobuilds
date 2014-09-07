# encoding=utf8
from rebranch_deployment.tools.config.parsers.redis import RedisConfigParser


class ConstanceBaseSettings(object):
    CONSTANCE_BACKEND = 'constance.backends.redisd.RedisBackend'

    CONSTANCE_CONFIG = {
        'CURRENT_GAME_VERSION': (u'2.1.0', u'Текущая версия игры'),
    }


class ConstanceProductionSettings(ConstanceBaseSettings):
    CONSTANCE_REDIS_CONNECTION = RedisConfigParser().get_config_object().geturl()