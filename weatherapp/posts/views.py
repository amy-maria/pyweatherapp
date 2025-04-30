from django.shortcuts import render, get_object_or_404, HttpResponse
from .models import Post


# Create your views here.
def posts_list(request):
    posts = Post.objects.all().order_by("-date")
    return render(request, "posts/posts_list.html", {"posts": posts})


def post_page(request, slug):
    # return HttpResponse(f"Slug: {slug}")
    post = get_object_or_404(Post, slug=slug)
    return render(request, "posts/post_page.html", {"post": post})
