from rest_framework import serializers
from blog.models import Post

class PostSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.username', read_only=True)
    category = serializers.CharField( read_only=True)
    class Meta:
        model = Post
        fields = ('id', 'title','author','excerpt','content','category','status','slug','published')
