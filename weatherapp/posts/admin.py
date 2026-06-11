from django.contrib import admin
from .models import Post

# Register your models here.
admin.site.register(Post)


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "date")  # Customize fields to show in the list
    prepopulated_fields = {"slug": ("title",)}  # Auto-fill slug from title
