from django.urls import path
from .views import get_post, create_post, delete_post, update_post


urlpatterns = [
    path('create', create_post, name='create_post'),
    path('<int:id_post>', get_post, name='post'),
    path('<int:id_post>/delete', delete_post, name='delete_post'),
    path('<int:id_post>/update', update_post, name='update_post')
]
