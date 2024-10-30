from django.urls import path
from core import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('',views.getRoutes,name="getRoutes"),
    path('users/register/',views.registerUser,name='register'),
    path('users/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('products/',views.getProducts,name="getProducts"),
    path('user/profile/',views.getUserProfiles,name="getUserProfiles"),
    path('products/<str:pk>',views.getProduct,name="getProduct"),
    path('users/',views.getUsers,name="getUsers"),


    # path('', views.home, name="home"),
    # path('about', views.about, name="about"),
    # path('contact', views.contact, name="contact"),
]


