
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('blog/', include('blog.urls')),
    path('orders/', include('order.urls')),
    path('user/', include('userauths.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
     path('accounts/', include('allauth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


### TEST ###

# handler404 = 'core.views.error_404'
# handler500 = 'core.views.error_500'