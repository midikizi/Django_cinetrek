from django.urls import path
from .views import *

urlpatterns = [
    path('logout/user/', logout_user, name="logout"),
    path('login/', login_user, name="login"),
    path('register/client/', login_user, name="login"),
    path('test-token/', login_user, name="login"),
]
