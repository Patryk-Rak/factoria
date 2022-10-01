from django.contrib import admin
from django.urls import path, include


from django.conf import settings
from django.conf.urls.static import static
from website.views import homepage_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('factoria.apps.accounts.urls')),
    path('', homepage_view, name="homepage"),
    path('product/', include('products.urls')),
    path('business/', include('business.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

