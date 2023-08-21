from django.urls import path
from .views import create_post, post_list, moderate_posts, ban_user, post_detail

urlpatterns = [
    path('create/', create_post, name='create_post'),
    path('list/', post_list, name='post_list'),
    path('moderate/', moderate_posts, name='moderate_posts'),
    path('ban/<int:user_id>/', ban_user, name='ban_user'),
    path('post/<int:post_id>', post_detail, name='post_detail'),
]
