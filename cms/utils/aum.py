import django
if django.VERSION >= (1, 5):
    from django.contrib.auth import get_user_model #pylint: disable=W0611
else:
    from django.contrib.auth.models import User
    get_user_model = lambda: User
