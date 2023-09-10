from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main_page.urls')),
    path('auth/', include('auth_regist.urls')),
    path('user/', include('for_users.urls')),
    path('upload/', include('for_admin.urls')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
