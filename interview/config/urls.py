from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

import debug_toolbar

apipatterns_v1 = [
    path('cart/', include('cart.api.v1.urls')),
    path('order/', include('orders.api.v1.urls')),
    # url(r'^auth/', include('djoser.urls')),
    path('', include('products.api.v1.urls')),
]

apipatterns_v2 = [
]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(apipatterns_v1)),
    url('api/v1/social-auth/', include('social_django.urls', namespace='social')),
    path('__debug__/', include(debug_toolbar.urls)),
]
