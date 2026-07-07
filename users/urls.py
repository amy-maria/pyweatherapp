from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "users"  # designates urlpatters are inside the posts app

urlpatterns = [
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
]
