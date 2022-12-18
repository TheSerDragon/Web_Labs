from django.contrib import admin
from games import views as game_views
from django.urls import include, path
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter()
router.register(r'games', game_views.GameViewSet, basename='game_list')
router.register(r'genres', game_views.GenreViewSet, basename='genre_list')
router.register(r'platforms', game_views.PlatformViewSet, basename='platformer_list')
router.register(r'publishers', game_views.PublisherViewSet, basename='publisher_list')
router.register(r'users', game_views.UsersViewSet, basename='users')
router.register(r'order_status', game_views.OrderStatusViewSet)
router.register(r'orders', game_views.OrderViewSet, basename='order')
router.register(r'cart', game_views.CartViewSet, basename='cart')
router.register(r'current_cart', game_views.CurrentCart, basename='game_in_cart')


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('admin/', admin.site.urls),
    path(r'gamePricing/', game_views.get_game_pricing),
    path(r'reg_new_user/', game_views.reg_new_user),  # ok
    path(r'login/', game_views.login_user),  # ok
    path(r'logout/', game_views.logout_user),  # ok
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
