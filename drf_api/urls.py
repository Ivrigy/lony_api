from django.contrib import admin
from django.urls import path, include
from .views import root_route, logout_route
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path("", root_route),
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("dj-rest-auth/logout/", logout_route),
    path("dj-rest-auth/", include("dj_rest_auth.urls")),
    path(
        "dj-rest-auth/registration/",
        include("dj_rest_auth.registration.urls"),
    ),
    path(
        "dj-rest-auth/token/refresh/",
        TokenRefreshView.as_view(),
        name="token_refresh",
    ),
    path("profiles/", include("profiles.urls")),
    path("posts/", include("posts.urls")),
    path("comments/", include("comments.urls")),
    path("likes/", include("likes.urls")),
    path("followers/", include("followers.urls")),
]
