class TestDatabaseSettings(object):
    @property
    def DATABASES(self):
        databases = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3'
            },
        }
        return databases


class DevelopmentDatabaseSettings(object):
    @property
    def DATABASES(self):
        databases = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql_psycopg2',
                # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
                'NAME': 'diablobuilds', # Or path to database file if using sqlite3.
                'USER': 'diablobuilds', # Not used with sqlite3.
                'PASSWORD': None, # Not used with sqlite3.
                'HOST': 'localhost', # Set to empty string for localhost. Not used with sqlite3.
                'PORT': 5432, # Set to empty string for default. Not used with sqlite3.
            },
        }
        return databases


class StagingDatabaseSettings(object):
    @property
    def DATABASES(self):
        databases = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql_psycopg2',
                # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
                'NAME': u'docker',  # Or path to database file if using sqlite3.
                'USER': u'docker',  # Not used with sqlite3.
                'PASSWORD': u'docker',  # Not used with sqlite3.
                'HOST': 'diablobuilds-postgresql',  # Set to empty string for localhost. Not used with sqlite3.
                'PORT': 5432,  # Set to empty string for default. Not used with sqlite3.
            },
        }
        return databases