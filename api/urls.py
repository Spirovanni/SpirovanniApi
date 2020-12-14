from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import CardViewSet, RatingViewSet
# from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register('cards', CardViewSet)
router.register('Ratings', RatingViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('api/', include('api.urls')),
    # path('auth/', obtain_auth_token),
]