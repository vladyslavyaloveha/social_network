from social_network.apps.activity.models import UserActivity


class LastActiveMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = request.user
        if user.is_authenticated:
            UserActivity.objects.create(url=request.build_absolute_uri(), user=user)
        return self.get_response(request)
