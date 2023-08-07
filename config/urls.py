
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from post.views import home_view


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', home_view, name='home_view'),
    path('posts/', include('post.urls', namespace='post')),
    path('user/', include('user.urls', namespace='user') ),
    
]
