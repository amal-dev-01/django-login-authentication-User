from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
urlpatterns = [
    path('',views.signup_page,name='signup'),
    path('login/',views.login_page,name='login'),
    path('home/',views.home_page,name='home'),
    path('logout/',views.logout_page,name='logout'),
]
