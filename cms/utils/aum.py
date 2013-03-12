import django
from django.conf import settings
if django.VERSION >= (1, 5):
    from django.contrib.auth import get_user_model #pylint: disable=W0611
    get_auth_model_name = lambda: settings.AUTH_USER_MODEL
else:
    from django.contrib.auth.models import User
    get_user_model = lambda: User
    get_auth_model_name = lambda: 'auth.User'
