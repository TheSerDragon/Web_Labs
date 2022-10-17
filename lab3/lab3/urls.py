from django.contrib import admin
from games import views as game_views
from genres import views as genre_views
from platforms import views as platform_views
from publishers import views as publisher_views
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'games', game_views.GameViewSet)
router.register(r'genres', genre_views.GenreViewSet)
router.register(r'platforms', platform_views.PlatformViewSet)
router.register(r'publishers', publisher_views.PublisherViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('admin/', admin.site.urls),
]
