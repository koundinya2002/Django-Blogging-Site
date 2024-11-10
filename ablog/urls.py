from django.contrib import admin
from django.urls import path, include, re_path
# from django.contrib.auth import views as auth_views
from members.views import PasswordsChangeView
from django.conf import settings
from django.conf.urls.static import static
from api_handles import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('theblog.urls')),
    path('auth/',include('django.contrib.auth.urls')),
    path('', include('members.urls')),
    # path('<int:id>/password/', auth_views.PasswordChangeView.as_view()),
    path('<int:uid>/password/', PasswordsChangeView.as_view()),
    path('api/', include('api_handles.urls')),
    re_path('login/', views.login, name="api_login"),
    re_path('signup/', views.signup, name="api_signup"),
    re_path('test_token/', views.test_token),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
