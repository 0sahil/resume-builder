
from django.urls import path,include
from . import views

urlpatterns = [
   path('login/',views.loginPage, name='login'),
    path('register/',views.registerPage,name='register'),
    # path('',views.home, name='home'),
    path('logout/',views.logoutUser,name='logout')
]