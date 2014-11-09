# encoding=utf8
from jetee_tools.service_resolvers import RedisJeteeServiceConfigResolver


class ConstanceBaseSettings(object):
    CONSTANCE_CONFIG = {
        'CURRENT_GAME_VERSION': (u'2.1.0', u'Текущая версия игры'),
    }


class ConstanceDevelopmentSettings(ConstanceBaseSettings):
    CONSTANCE_REDIS_CONNECTION = 'redis://localhost:6379/0'


class ConstanceProductionSettings(ConstanceBaseSettings):
    CONSTANCE_REDIS_CONNECTION = RedisJeteeServiceConfigResolver(host=u'mindgames-redis').render()