from django.contrib import admin
from django.urls import path
from post.views import  myposts_view , add_post , post_detail , post_update , delete

app_name ='post'

urlpatterns = [
    path('myposts/' , myposts_view, name='myposts_view' ),
    path('add-post/' , add_post, name='add_post' ),
    path('myposts/<int:id>' , post_detail, name='post_detail' ),
    path('myposts/<int:id>/update' , post_update, name='post_update' ),
    path('myposts/<int:id>/delete' , delete, name='delete' ),
   
]
