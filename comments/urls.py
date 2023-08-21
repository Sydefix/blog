from django.urls import path
from .views import add_comment, remove_comment

urlpatterns = [
    path('add/<int:post_id>/', add_comment, name='add_comment'),
    path('remove/<int:comment_id>/', remove_comment, name='remove_comment'),
]
