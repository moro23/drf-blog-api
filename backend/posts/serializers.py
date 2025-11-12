from rest_framework import serializers 
from .models import Post 

class PostSerializer(serializers.ModelSerializer):

    class Meta:

        ## lets make the author field read-only
        author = serializers.StringRelatedField(read_only=True)

        fields = ('id', 'author', 'title', 'body', 'created_at')
        model = Post 

