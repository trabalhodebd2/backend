from rest_framework.routers import DefaultRouter

from .viewsets import *

user_router = DefaultRouter()
user_router.register('users', UserViewset, basename="api-users")
