from django.urls import path
from . import views
urlpatterns = [
    path('', views.PostApi.as_view(), name='post'),
    path('<int:pk>', views.PostApi.as_view(), name='post'),
    path('<filename>', views.PostApi.as_view(), name='post'),


]