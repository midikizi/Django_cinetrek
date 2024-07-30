from rest_framework.authtoken.views import obtain_auth_token

from django.urls import path
from .views import *

urlpatterns = [
    path('logout/user/', logout_user),
    path('login/', login_user),
    path('sign-up/client/', register_user_client),
    path('sign-up/gerant/', register_user_gerant),
    path('api-auth-token/', obtain_auth_token),
]