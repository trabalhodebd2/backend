from django.urls import path, include

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .api.routers import user_router

urlpatterns = [
    # login router
    path("api/login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/refresh_token/", TokenRefreshView.as_view(), name="token_refresh"),
    # user router
    path("api/", include(user_router.urls)),
]
