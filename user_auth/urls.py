from django.urls import path
from . import views

urlpatterns = [
    path('',views.user_login,name='login'),
    path('index/',views.index,name='index'),
    path('admin_view/',views.admin_view,name='admin_view'),
    path('register/',views.signup,name='register'),
    path('admin_signup/',views.admin_signup,name='admin_signup'),
    path('logout/',views.user_logout,name='logout'),
    
    

    
]
