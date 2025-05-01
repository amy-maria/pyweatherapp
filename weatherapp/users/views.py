from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)  # will validate form
        if form.is_valid():
            form.save()
            return redirect("posts:list")
    else:
        form = UserCreationForm()
    form = UserCreationForm()
    return render(request, "users/register.html", {"form": form})
