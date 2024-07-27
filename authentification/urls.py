from django.urls import path
from .views import *

urlpatterns = [
    path('logout/user/', logout_user, name="logout"),
    path('login/', login_user, name="login"),
    path('sign/up/client/', register_user_client, name="register_user_client"),
    path('test-token/', test_token, name="test_token"),
]
