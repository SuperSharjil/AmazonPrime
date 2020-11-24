from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserDetail, name="Details"),
    path('login/', views.AfterLogin, name="AfterLogin"),
    path('logout/', views.Logout, name="Logout"),
    path('signup/', views.Signup, name="Signup"),
    path('signing-up/', views.AfterSignup, name="AfterSignup"),
    path('change-password/', views.ChangePassword, name="ChangePassword"),
    path('changing-password/', views.ChangingPassword, name="ChangingPassword"),
    path('history/', views.History, name="History"),
    path('payment/', views.Payment, name="Payment"),
    path('payment/<int:id>/', views.AfterPayment, name="AfterPayment"),
    #path('changeprofile/', views.index, name="index"),
]
