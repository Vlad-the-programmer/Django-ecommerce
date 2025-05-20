from django.urls import path
from allauth.account import views as account

from . import views
from .forms import UserLoginForm

app_name = "userauths"

urlpatterns = [

	# User Auths
	path("sing-up/", views.register_view, name="sign-up"),

    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('login/', account.LoginView.as_view(
                                            #    form_class=UserLoginForm,
                                            ), name='sign-in'),
    path('logout/', account.LogoutView.as_view(), name='sing-out'),
    path('profile/detail/<int:pk>/', views.ProfileDetail.as_view(),
                                                        name='profile-detail'),
    path('profile/delete/<int:pk>/', views.ProfileDelete.as_view(),
                                                        name='profile-delete'),
    path('profile/update/<int:pk>/', views.ProfileUpdate.as_view(),
                                                        name='profile-update'),
    
    path('forgot-password/', views.forgotPassword, name='forgotPassword'),
    path('reset-password-validate/<int:pk>', views.reset_password_validate,
         name='reset-password-validate'),
    path('reset-password/<int:pk>', views.resetPassword, name='resetPassword'),
    
	# User Account
	path("account/", views.account, name="account"),
]