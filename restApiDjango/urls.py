from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from user.views import UserViewSet, ListUser

router = routers.DefaultRouter()
router.register('user', UserViewSet, basename='user')


urlpatterns = [
    path('users/', include('user.urls')),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('user-list', ListUser.as_view())
]
