from .views import user_profile, login_user, main, logout_user
from django.urls import path 

urlpatterns = [
    path('', user_profile, name='user_profile'),
    path('login_user/', login_user, name='login_user'),
    path('main/', main, name='main'),
    path('logout_user/', logout_user, name='logout_user'),
]

