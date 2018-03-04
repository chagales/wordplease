from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from django.utils import timezone


from blogging.models import Post
from blogging.permissions import PostPermission, CategoriesPermission
from blogging.serializers import PostSerializer, PostListSerializer, CategorySerializer


class PostListAPI(ListCreateAPIView):
  queryset = Post.objects.all()
  permission_classes = (IsAuthenticatedOrReadOnly,)
  def post(self, request):
          if request.user.is_authenticated:
              request.data['user']=request.user.id
              serializer = PostSerializer(data=request.data)
              if serializer.is_valid():
                  post = serializer.save()
                  return Response(serializer.data, status=201)
              else:
                  return Response(serializer.errors, status=400)
          else:
              return Response({"No tiene permisos":"no tiene permisos para realizar esta accion"},status=403)

class PostDetailAPI(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [PostPermission]

    def get(self, request, username, pk):
      post = get_object_or_404(Post, pk=pk, user__username=username)
      if post.published_at <= timezone.now():
        serializer = PostSerializer(post)
        return Response(serializer.data)
      elif str(request.user) == username or request.user.is_superuser and post.published_at >= timezone.now():
        serializer = PostSerializer(post)
        return Response(serializer.data)
      else:
        return Response({"No tiene permisos":"no tiene permisos para realizar esta accion"},status=403)

    def put(self, request, username, pk):
      post = get_object_or_404(Post, pk=pk)
      self.check_object_permissions(request, post)
      serializer = PostSerializer(post, data=request.data)
      if serializer.is_valid():
        post = serializer.save()
        return Response(serializer.data, status=202)
      else:
        return Response(serializer.errors, status=400)

