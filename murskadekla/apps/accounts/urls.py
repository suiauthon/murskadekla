from django.urls import path, re_path
from django.contrib.auth import views as auth_views

from . import views

app_name = "accounts"
urlpatterns = [
    path("profile", views.ProfileView.as_view(), name="profile"),
    # Django Auth
    path(
        "login",
        views.LoginView.as_view(template_name="accounts/login.html"),
        name="login",
    ),
    path("logout", auth_views.LogoutView.as_view(), name="logout"),
    path("register", views.RegisterView.as_view(), name='register'),
    re_path(r'^email/confirm/(?P<key>[0-9A-Za-z]+)/$',
            views.AccountEmailActivateView.as_view(),
            name='email-activate'),
    path('email/resend-activation',
            views.AccountEmailActivateView.as_view(),
            name='resend-activation'),
]

#accounts/login
#logoug
#password_change
#password_change/done
#password_reset
#password_reset/done
#reset
#reset/done
#path("", include('django.contrib.auth.urls'))