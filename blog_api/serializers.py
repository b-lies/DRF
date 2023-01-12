from rest_framework import serializers
from blog.models import Post

class PostSerializer(serializers.ModelSerializer):
    #author = serializers.CharField( read_only=True)
    category = serializers.CharField(source= "category.name",read_only=True)
    class Meta:
        model = Post
        fields = ('id', 'title','author','excerpt','content','image','category','status','slug','published')
