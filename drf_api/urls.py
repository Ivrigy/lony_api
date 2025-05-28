# drf_api/urls.py
from django.contrib import admin
from django.urls import path, include
from .views import root_route, logout_route

# dj-rest-auth’s cookie‐based refresh
from dj_rest_auth.jwt_auth import get_refresh_view
# SimpleJWT’s verify (dj-rest-auth doesn’t ship its own in v7.0)
from rest_framework_simplejwt.views import TokenVerifyView

urlpatterns = [
    path('', root_route),
    path('admin/', admin.site.urls),

    path('api-auth/', include('rest_framework.urls')),

    path('dj-rest-auth/logout/', logout_route),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),

    path(
        'dj-rest-auth/token/refresh/',
        get_refresh_view().as_view(),
        name='token_refresh'
    ),
    path(
        'dj-rest-auth/token/verify/',
        TokenVerifyView.as_view(),
        name='token_verify'
    ),

    path('', include('profiles.urls')),
    path('', include('posts.urls')),
    path('', include('comments.urls')),
    path('', include('likes.urls')),
    path('', include('followers.urls')),
]
