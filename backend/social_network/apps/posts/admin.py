from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    readonly_fields = (
        "pk",
        "description",
        "likes",
        "created_at",
        "updated_at",
        "user",
    )

    list_display = (
        "pk",
        "description",
        "created_at",
        "updated_at",
        "user",
    )
    list_display_links = ("pk",)
    search_fields = (
        "pk",
        "user__username",
    )
