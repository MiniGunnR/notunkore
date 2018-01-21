from django.urls import path

from django.contrib.auth.views import login, logout_then_login

from . import views


app_name = 'core'
urlpatterns = [
    path('', login, kwargs={'redirect_authenticated_user': True}, name='my_login'),
    path('logout/', logout_then_login, name='my_logout'),

    path('register/', views.register, name='register'),
]
