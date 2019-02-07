from django.urls import path
from myapp.views import *

urlpatterns = [
    path('home/', home,name="home"),
    path('signin/',signin,name="signin"),
    path('signup/',signup,name="signup"),
    path('google-signup/',google_signup,name="google-signup"),
    path('form-api/',form,name="form-api"),
    path('logout/',logout_user,name="logout"),
    path('users/<str:role>/',users,name="users")
]