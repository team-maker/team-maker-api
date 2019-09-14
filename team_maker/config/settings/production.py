from .common import *  # noqa
from datadog import initialize
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

options = {
    'api_key': env('DATADOG_API_KEY'),
    'app_key': env('DATADOG_APP_KEY')
}

initialize(**options)
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('DJANGO_SECRET_KEY')

sentry_sdk.init(
    dsn=env('SENTRY_DSN'),
    integrations=[DjangoIntegration()]
)
