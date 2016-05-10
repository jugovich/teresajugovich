"""
Django settings for Coding project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""
import os
from sqlalchemy import orm

#detect env
_config = 'dev'
#import env settings
config_module = __import__('config.%s' % _config, globals(), locals(), 'iCode')

# Load the config settings properties into the local scope.
for setting in dir(config_module):
    if setting == setting.upper():
        locals()[setting] = getattr(config_module, setting)


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&vvvsao=0_g#b5xrlx(w!1#u+)sdafsdfsd0$dl^zn*s)+=(4ri1xsjk-$5'

# SECURITY WARNING: don't run with debug turned on in production!
TEMPLATE_DEBUG = DEBUG

# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #internal apps
    'blisschild',
    #third-party-apps
)

ROOT_URLCONF = 'blisschild.urls'
#WSGI_APPLICATION = 'blisschild.wsgi.application'
SITE_ID = 1

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/Chicago'

USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(os.path.join(__file__, '..', 'blisschild/static')),
    os.path.join(os.path.join(__file__, '..', 'static')),
)


# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)


TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    os.path.join(os.path.join(__file__, '..', 'templates')),
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

#AUTH_PROFILE_MODULE = 'django.contrib.auth.models.User'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.

#LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'filters': {
#         'require_debug_false': {
#             '()': 'django.utils.log.RequireDebugFalse'
#         }
#     },
#     'formatters': {
#         'verbose': {
#             'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
#             'datefmt': "%d/%b/%Y %H:%M:%S"
#         },
#         'simple': {
#             'format': '%(levelname)s %(message)s'
#         },
#     },
#     'handlers': {
#         'mail_admins': {
#             'level': 'ERROR',
#             'filters': ['require_debug_false'],
#             'class': 'django.utils.log.AdminEmailHandler'
#         },
#         'debug': {
#             'level': 'DEBUG',
#             'class': 'logging.FileHandler',
#             'filename': r'%s/debug.log' % LOGDIR,
#             'formatter': 'verbose',
#         },
#         'error': {
#             'level': 'DEBUG',
#             'class': 'logging.FileHandler',
#             'filename': r'%s/error.log' % LOGDIR,
#             'formatter': 'verbose',
#         },
#         'search': {
#             'level': 'DEBUG',
#             'class': 'logging.FileHandler',
#             'filename': r'%s/search.log' % LOGDIR,
#             'formatter': 'verbose',
#         },
#
#
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['error'],
#             'level': 'ERROR',
#             'propagate': True,
#         },
#         'django.request': {
#             'handlers': ['error'],
#             'level': 'ERROR',
#             'propagate': True,
#         },
#
#         'search': {
#             'handlers': ['search'],
#             'level': 'DEBUG',
#             'propagate': True,
#         },
#
#     }
# }
