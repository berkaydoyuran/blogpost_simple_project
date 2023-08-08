from django.contrib import admin
from django.urls import path
from post.views import home_view , myposts_view , add_post , post_detail , post_duzenle , silme , read_only

app_name ='post'

urlpatterns = [
    path('myposts/' , myposts_view, name='myposts_view' ),
    path('add-post/' , add_post, name='add_post' ),
    path('myposts/<int:id>' , post_detail, name='post_detail' ),
    path('posts/<int:id>' , read_only, name='read_only' ),
    path('myposts/<int:id>/update' , post_duzenle, name='post_duzenle' ),
    path('myposts/<int:id>/sil' , silme, name='silme' ),
   
]
