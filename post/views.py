from django.shortcuts import render , redirect 
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import Http404
from django.shortcuts import get_object_or_404
from .models import Post
from .forms import PostForm
from slugify import slugify


def home_view(request):
    posts = Post.objects.all()
    context = dict(
        posts = posts
    )

    return render(request, 'allposts.html', context)

@login_required(login_url="/user/login")
def myposts_view(request):
    posts = Post.objects.all()
    posts = Post.objects.filter(user= request.user)

    context = dict(
        posts =posts
    )

    return render(request, 'post/myposts.html', context)

@login_required(login_url="/user/login")
def add_post(request):
    form = PostForm(request.POST or None, request.FILES or None)
    
    if form.is_valid():
        post = form.save(commit = False)
        post.user = request.user
        post.save()

        messages.success(request, 'Aferin laaaan')
        return redirect('/')
    context = {
        'form': form
    }
    return render(request, 'post/add_post.html', context)

@login_required(login_url="/user/login")
def post_detail(request  , id):
    item = get_object_or_404(Post , pk = id , user = request.user)
    context = dict(
        item = item
    )
    return render(request, 'post/post_detail.html' , context)

@login_required(login_url="/user/login")
def post_duzenle(request, id):

    post  = get_object_or_404(Post, id=id )
    form = PostForm(request.POST or None , request.FILES or None, instance = post)
     
    if form.is_valid():
        post = form.save(commit = False)
        post.user = request.user
        post.save()

        messages.success(request, 'Aferin laaaan duzenledin')
        return redirect('user:login')

    context = dict(
        form = form ,
    )

    return render(request, 'post/post_update.html', context)