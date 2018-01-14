from rest_framework import serializers

from blogging.models import Post, Category
from users.serializers import UserSerializer


class PostListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ["id", "title", "image","intro","publication_date"]


class PostSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'
