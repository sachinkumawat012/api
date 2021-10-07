from .views import RegisterAPI
from django.urls import path
from knox import views as knox_views
from .views import LoginAPI

from django.urls import path
from django.urls.conf import include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

#creating default router
router = DefaultRouter()

#register profile viewset with routers
router.register('', views.ProfileViewSet, basename='profile')

urlpatterns = [

    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('slogoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),

    path('', include(router.urls)),

    

]



    # path('<filename>', views.ProfileView.as_view(), name='profile'),
    # path('<int:pk>', views.ProfileView.as_view(), name='profile'),
    # path('', views.ProfileView.as_view(), name='profile'),
    ## knox token
    # path('register/', views.RegisterAPIView.as_view(), name='register'),
    # path('login/', TokenObtainPairView.as_view(), name='login_view'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh_view'),
    # path('logout/', views.LogoutView.as_view(), name='auth_logout'),