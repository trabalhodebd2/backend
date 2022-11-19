from django.urls import path, include


from .api.routers import hemo_router

urlpatterns = [
    path("api/", include(hemo_router.urls)),
]
