from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', include('marketing.url',namespace='marketing')),
    path('admin/', admin.site.urls),
]

urlpatterns +=  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# from webs.views.Home import *
#
#
# handler404 = "webs.views.Home.handle_not_found"
# handler500 = "webs.views.Home.handle_server_error"
