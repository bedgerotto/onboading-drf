from django.views.decorators import csrf
from library.models import Category, Author, Book
from rest_framework import viewsets, permissions
from library.serializers import CategorySerializer, AuthorSerializer, BookSerializer
from django.views.decorators.csrf import csrf_exempt, csrf_protect, requires_csrf_token, ensure_csrf_cookie
from django.middleware.csrf import CsrfViewMiddleware
from django.utils.decorators import method_decorator
from rest_framework import exceptions

from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from library.utils import generate_access_token, generate_refresh_token
from django.contrib.auth import get_user_model
from library.authentication import SafeJWTAuthentication


@api_view(['POST'])
@permission_classes([AllowAny])
@ensure_csrf_cookie
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    response = Response()
    if (username is None) or (password is None):
        raise exceptions.AuthenticationFailed(
            'username and password required')

    User = get_user_model()
    user = User.objects.filter(username=username).first()
    if(user is None):
        raise exceptions.AuthenticationFailed('user not found')
    if (not user.check_password(password)):
        raise exceptions.AuthenticationFailed('wrong password')

    access_token = generate_access_token(user)
    refresh_token = generate_refresh_token(user)

    response.set_cookie(key='refreshtoken', value=refresh_token, httponly=True)
    response.data = {
        'access_token': access_token
    }

    return response

class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint for categorys
    """
    queryset = Category.objects.all().order_by('-created_at')
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]

class AuthorViewSet(viewsets.ModelViewSet):
    """
    API endpoint for authors
    """
    queryset = Author.objects.all().order_by('-created_at')
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticated]

class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint for books
    """
    queryset = Book.objects.all().order_by('-release_date')
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
