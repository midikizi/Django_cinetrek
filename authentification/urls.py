from django.urls import path
from .views import *

urlpatterns = [
    path('logout/user/', logout_user),
    path('login/', login_user),
    path('sign-up/client/', register_user_client),
    path('sign-up/gerant/', register_user_gerant),
    path('test-view/', protected_view),
]