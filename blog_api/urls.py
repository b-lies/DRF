from .views import AdminPost,PostList,PostListfilter
from django.urls import path
from rest_framework.routers import DefaultRouter


app_name = 'blog_api'

router = DefaultRouter()

router.register('v1', PostList , basename='post')
router.register('search', PostListfilter , basename='postsearch')
router.register('admin', AdminPost, basename='postadmin')
urlpatterns = router.urls
