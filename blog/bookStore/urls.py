from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("books/", views.books, name="books"),
    path("customer/<str:pk>", views.customer, name="customer"),
    path("create/<str:pk>", views.create, name="create"),
    path("update/<str:pk>", views.update, name="update"),
    path("delete/<str:pk>", views.delete, name="delete"),
    path("register/", views.register, name="register"),
    path("login/", views.UserLogin, name="login"),
    path("logout/", views.userLogout, name="logout"),
    path("user/", views.userProfile, name="user-profile"),
    path("profile/", views.profileInfo, name="profile_info"),
    path(
        "reset-password/",
        auth_views.PasswordResetView.as_view(template_name="bookStore/reset_password.html"),
        name="reset_password",
    ),
    path(
        "reset-password-sent/",
        auth_views.PasswordResetDoneView.as_view(template_name="bookStore/reset_password_sent.html"),
        name="password_reset_done",
    ),
    # <uidb64> for the user id in base 64
    # <token> is a token that is generated by django to identify the user means that the user is valid
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(template_name="bookStore/reset_password_form.html"),
        name="password_reset_confirm",
    ),
    path(
        "reset-password-complete/",
        auth_views.PasswordResetCompleteView.as_view(template_name="bookStore/reset_password_complete.html"),
        name="password_reset_complete",
    ),
]
# auth_views.PasswordResetView.as_view(): for the reset password page
# auth_views.PasswordResetDoneView.as_view(): for the reset password sent page
# auth_views.PasswordResetConfirmView.as_view(): for the reset password page after the user click on the link in the email
# auth_views.PasswordResetCompleteView.as_view(): for the reset password complete page
