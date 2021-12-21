from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.urls.conf import include
from apps.core.views import frontpage, privacy, terms, plans, signup
from apps.userprofile.views import myaccount, edit_profile

urlpatterns = [
    path("", frontpage, name="frontpage"),
    path("privacy/", privacy, name="privacy"),
    path("terms/", terms, name="terms"),
    path("plans/", plans, name="plans"),
    path("admin/", admin.site.urls),
    # Auth
    path("signup/", signup, name="signup"),
    path(
        "login",
        auth_views.LoginView.as_view(template_name="core/login.html"),
        name="login",
    ),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("myaccount/", myaccount, name="myaccount"),
    path("myaccount/edit_profile", edit_profile, name="edit_profile"),
    path("myaccounts/teams/", include("apps.team.urls")),
]
