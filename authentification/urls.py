from rest_framework.authtoken.views import obtain_auth_token

from django.urls import path
from .views import *

urlpatterns = [
    path('logout/user/', logout_user),
    path('login/', LoginView.as_view()),
    path('sign-up/client/', RegisterClient.as_view()),
    path('sign-up/gerant/', RegisterGerant.as_view()),
    path('api-auth-token/', obtain_auth_token),
]