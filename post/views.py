from django.shortcuts import render , redirect 
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import get_object_or_404
from .models import Post
from .forms import PostForm



def home_view(request):
    posts = Post.objects.filter(is_deleted=False) #order_by kullanilabilir
    context = dict(
        posts = posts
    )

    return render(request, 'home_page.html', context)

@login_required(login_url="/user/login")
def myposts_view(request):
    posts = Post.objects.filter(is_deleted= False, user= request.user)

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

        messages.success(request, 'Bravo Post Ekledin!')
        return redirect('/')
    context = {
        'form': form
    }
    return render(request, 'post/add_post.html', context)

def post_detail(request  , id): 
    item = get_object_or_404(Post, pk = id )
    context = dict(
        item = item,
        is_editable = True if item.user == request.user else False
    )
    return render(request, 'post/post_detail.html' , context)

@login_required(login_url="/user/login")
def post_update(request, id):

    post  = get_object_or_404(Post, id=id )
    form = PostForm(request.POST or None , request.FILES or None, instance = post)
     
    if form.is_valid():
        post = form.save(commit = False)
        post.user = request.user
        post.save()

        messages.success(request, 'Bravo Postunu Düzenledin!')
        return redirect('post:myposts_view')

    context = dict(
        form = form ,
    )

    return render(request, 'post/post_update.html', context)

@login_required(login_url="/user/login")
def delete(request,  id):
    post = get_object_or_404(Post, id=id)

    post.delete_from_page()
    return redirect('/')