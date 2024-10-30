from django.contrib import admin
from django.urls import path, include
from members.views import PasswordsChangeView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('theblog.urls')),
    path('',include('django.contrib.auth.urls')),
    path('', include('members.urls')),
    path('<int:uid>/password/', PasswordsChangeView.as_view())

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
