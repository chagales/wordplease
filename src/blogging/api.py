from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from blogging.models import Post
from blogging.permissions import PostPermission, CategoriesPermission
from blooging.serializers import PostSerializer, PostListSerializer, CategorySerializer


class PostListAPI(ListCreateAPIView):
    queryset = Post.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_serializer_class(self):
        return PostListSerializer if self.request.method == "GET" else PostSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PostDetailAPI(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [PostPermission]

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
