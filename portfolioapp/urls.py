from django.urls import path, include
from .views import CustomTokenObtainPairView, UserRegisterViewSet, UserDetailGetOrUpdate, GetGeographyLocation
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register("get-user-detail", UserDetailGetOrUpdate, basename="get-user-detail")

urlpatterns = [
    path('signin/', CustomTokenObtainPairView.as_view(), name='signin'),
    path('signup/', UserRegisterViewSet.as_view(), name="signup"),
    path('map/', GetGeographyLocation.as_view(), name="map"),
    # path('all-users/', UserGetView.as_view(), name="all-user"),
    path('', include(router.urls)),
]
