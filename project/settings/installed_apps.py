# Application definition

DJANGO_BUILT_IN_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.gis",
]

THIRD_PARTY_APPS = [
    "imagekit",  # pip install django-imagekit
    "corsheaders",  # pip install django-cors-headers
    "rest_framework",  # pip install djangorestframework
    "rest_framework_simplejwt",  # pip install djangorestframework-simplejwt,
]

PROJECT_APPS = [
    "apps.auth_app",
    "apps.base_app",
    "apps.hemo",
]

INSTALLED_APPS = DJANGO_BUILT_IN_APPS + THIRD_PARTY_APPS + PROJECT_APPS

#  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #

AUTH_USER_MODEL = "auth_app.User"
