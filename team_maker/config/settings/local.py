from .common import *  # noqa

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('DJANGO_SECRET_KEY', default='1@)gllki#^%#%-kl7u@#8shzid9*&5a!pyt8#kh(o(d^sw@xt4')
