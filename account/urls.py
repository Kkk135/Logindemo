from django.urls import path
from .import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns =[
    path('',views.indexview,name="home"),
    path('dashboard/',views.dashboardview,name="dashboard"),
    path('login/',LoginView.as_view(),name="login_url"),
    path('register/',views.registerview,name="register_url"),
    path('logout/',LogoutView.as_view(next_page='dashboard'),name="logout_url"),

]
