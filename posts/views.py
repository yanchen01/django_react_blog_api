from rest_framework import viewsets

from .models import Post
from django.contrib.auth import get_user_model

from .permissions import IsAuthorOrReadOnly
from .serializer import PostSerializer, UserSerializer


# ListView and DetailView
class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# ListView and DetailView
class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
