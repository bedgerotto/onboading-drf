from django.urls import include, path
from django.conf.urls import url
from rest_framework import routers
from library import views

router = routers.DefaultRouter()
router.register(r'categories', views.CategoryViewSet)
router.register(r'authors', views.AuthorViewSet)
router.register(r'books', views.BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
    url(r'^library/login/$', views.login_view),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
