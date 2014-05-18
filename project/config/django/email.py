# coding: utf-8


class EmailSettings(object):
    EMAIL_SENDER = u'Сайт DiabloBuilds.ru <mail@diablobuilds.ru>'
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = u'smtp.yandex.ru'
    EMAIL_HOST_PASSWORD = u'dqsHa*Tz;kC68c'
    EMAIL_HOST_USER = u'mail@diablobuilds.ru'
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True