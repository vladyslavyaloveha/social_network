from django.contrib.auth import get_user_model
from django.db import models


class Post(models.Model):
    description = models.TextField(max_length=2200)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    likes = models.ManyToManyField(
        get_user_model(), blank=True, related_name="likes", through="Like"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Like(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
