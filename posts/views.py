from rest_framework import generics

from .models import Post
from .permissions import IsAuthorOrReadOnly
from .serializer import PostSerializer


# GET, POST
class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# GET, PUT, PATCH, DELETE
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
