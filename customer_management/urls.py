from django.urls import path
from . import views

urlpatterns= [
    path('', views.landing, name='landing'),
    path('login/', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout'),
    path('home/', views.home, name='home')
]