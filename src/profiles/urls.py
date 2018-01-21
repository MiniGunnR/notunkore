from django.urls import path

from . import views


app_name = 'profiles'
urlpatterns = [
    path('', views.redirect_to_profile, name='redirect_to_profile'),
    path('<int:pk>/', views.profile, name='profile'),
]
