from django.contrib import admin
from django.urls import path, include
# from django.contrib.auth import views as auth_views
from members.views import PasswordsChangeView

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('theblog.urls')),
    path('',include('django.contrib.auth.urls')),
    path('', include('members.urls')),
    # path('<int:id>/password/', auth_views.PasswordChangeView.as_view()),
    path('<int:uid>/password/', PasswordsChangeView.as_view())

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
