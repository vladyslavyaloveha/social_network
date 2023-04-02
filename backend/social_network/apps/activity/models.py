from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserActivity(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("User activity")
        verbose_name_plural = _("User activities")
