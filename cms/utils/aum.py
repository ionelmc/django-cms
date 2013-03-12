import django
if django.VERSION >= (1, 5):
    from django.contrib.auth import get_user_model #pylint: disable=W0611
else:
    from cms.utils.aum import get_user_model; User=get_user_model()
    get_user_model = lambda: User
