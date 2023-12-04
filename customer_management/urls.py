from django.urls import path
from . import views

urlpatterns= [
    path('', views.landing, name='landing'),
    path('login/', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),
    path('home/', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('show_record/<int:pk>', views.show_record, name='show_record'),
    path('delete_record/<int:pk>', views.delete_record, name='delete_record'),
    path('add_record/', views.add_record, name='add_record'),
    path('update_record/<int:pk>', views.update_record, name='update_record'),
]