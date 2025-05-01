from django.urls import path
from . import views

app_name = "users"  # designates urlpatters are inside the posts app

urlpatterns = [
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
]
