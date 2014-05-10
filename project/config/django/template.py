import os
from configurations import Configuration


class TemplateSettings(object):
    @property
    def TEMPLATE_CONTEXT_PROCESSORS(self):
        template_processors = Configuration.TEMPLATE_CONTEXT_PROCESSORS
        template_processors += (
            'django.contrib.auth.context_processors.auth',
            'django.core.context_processors.i18n',
            'django.core.context_processors.debug',
            'django.core.context_processors.media',
            'django.core.context_processors.request',
            'core.context_processors.current_game_version',
        )
        return template_processors

    TEMPLATE_LOADERS = (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader'
    )

    @property
    def TEMPLATE_DIRS(self):
        return (
            os.path.join(self.PROJECT_ROOT, 'templates'),
        )