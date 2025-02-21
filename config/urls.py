from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
 # path('admin/', admin.site.urls),
 # path('account/', include('account.urls', namespace='account')),
 #path('cart/', include('cart.urls', namespace='cart')),
 # path('orders/', include('orders.urls', namespace='orders')),
 # path('', include('store.urls', namespace='store')),
  path('i18n/', include('django.conf.urls.i18n')),  # Для смены языка
]

urlpatterns += i18n_patterns(
  path('admin/', admin.site.urls),
  path('account/', include('account.urls', namespace='account')),
  path('cart/', include('cart.urls', namespace='cart')),
  path('orders/', include('orders.urls', namespace='orders')),
  path('', include('store.urls', namespace='store')),
  path('blog/', include('blog.urls')),
#path('', include('store.urls')),  # Ваши основные URL
)

if settings.DEBUG:
  urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
