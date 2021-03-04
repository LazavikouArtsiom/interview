from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

authpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

apipatterns_v1 = [
    path('cart/', include('cart.api.v1.urls')),
    path('order/', include('orders.api.v1.urls')),
    path('auth/', include((authpatterns, 'auth'))),
    path('', include('products.api.v1.urls')),
]

apipatterns_v2 = [
]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include((apipatterns_v1, 'api_v1'), namespace='api_v1')),
]
