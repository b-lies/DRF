from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from blog.models import Post
from .serializers import PostSerializer

class PostList (viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter]
    filterset_fields = ['category']
    ordering_fields = ['published']

    #Get Post Instance by Slug Name
    def get_object(self, queryset=None,**kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Post, slug=item)

    #Define Custom QuerySet
    def get_queryset(self):
        return Post.objects.all()    

class PostListfilter (viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title','excerpt','content','slug']

    def get_queryset(self):
        return Post.objects.all()

# Post Admin

class AdminPost (viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    

    
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
#