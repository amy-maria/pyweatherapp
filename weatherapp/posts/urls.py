from django.urls import path
from . import views

app_name = "posts"  # designates urlpatters are inside the posts app

urlpatterns = [
    path("", views.posts_list, name="list"),
    path("new-post/", views.post_new, name="new-post"),  # required above slug
    path("<slug:slug>/", views.post_page, name="page"),
]
