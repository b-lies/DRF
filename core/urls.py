from django.contrib import admin
from django.urls import path,include
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #Project URLS
    path('admin/', admin.site.urls),
    path('', include('blog.urls',namespace='blog')),
    #Api Auth
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),   
    #Blog_API App
    path('api/', include('blog_api.urls',namespace='blog_api')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #API Documentation
    path('docs/', include_docs_urls(title='BlogAPI')),
    path('schema/', get_schema_view(
        title="BlogAPI",
        description="API for Blog Content",
        version="1.0.0"
    ), name='blogapi-schema'),


]

urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)