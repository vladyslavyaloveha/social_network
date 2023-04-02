from django.contrib import admin

from .models import UserActivity


@admin.register(UserActivity)
class UserActivityAdmin(admin.ModelAdmin):
    readonly_fields = (
        "pk",
        "url",
        "created_at",
        "user",
    )

    list_display = (
        "pk",
        "user",
        "created_at",
        "url",
    )
    list_display_links = ("pk",)
    search_fields = (
        "pk",
        "user__username",
    )
