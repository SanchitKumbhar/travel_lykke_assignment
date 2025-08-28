from django.contrib import admin
from django.urls import path,include
from authentication import views

urlpatterns = [
    path("authentication",views.render_authentication,name="authentication"),
    path("login",views.process_login,name="login"),
    path("signup",views.process_signup,name="signup"),
    path("",views.index,name="home"),
    path("logout",views.process_logout,name="logout"),

]