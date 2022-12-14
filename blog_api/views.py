from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from blog.models import Post
from .serializers import PostSerializer


class PostList (viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer

    #Get Post Instance by Slug Name
    def get_object(self, queryset=None,**kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Post, slug=item)

    #Define Custom QuerySet
    def get_queryset(self):
        return Post.objects.all()    



# class PostList (generics.ListCreateAPIView):
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     queryset = Post.postobjects.all()
#     serializer_class = PostSerializer  

# class PostDetail (generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
