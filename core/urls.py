from django.contrib import admin
from django.urls import path,include
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls',namespace='blog')),
    path('api/', include('blog_api.urls',namespace='blog_api')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('docs/', include_docs_urls(title='BlogAPI')),
    path('schema/', get_schema_view(
        title="BlogAPI",
        description="API for Blog Content",
        version="1.0.0"
    ), name='blogapi-schema'),

]
