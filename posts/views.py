from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm, PictureForm
from django.urls import reverse_lazy, reverse

from cloudinary.forms import cl_init_js_callbacks


# Create your views here.

def index(request):
    # if the method is POST
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        # If the form is valid
        if form.is_valid():
            #Yes, save
            form.save()

            # Redirect to Home
            return HttpResponseRedirect('/')

            # No, show error
        else:
            return HttpResponseRedirect(form.erros.as_json())

    posts = Post.objects.all().order_by('-created_at')[:20]

    # show
    return render(request, 'posts.html',
                  {'posts': posts})


# delete button to delete our posts


def delete(request, post_id):
    # Find post
    post = Post.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect('/')

# edit button to edit our posts


def edit(request, post_id):
    # Find post
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect(form.errors.as_json())

    form = PostForm
    # form = PostForm

    # show
    return render(request, 'edit.html', {'post': post, 'form': form})


# function for the like button for our posts
def Like(request, post_id):
    post = Post.objects.get(id=post_id)
    new_value = post.likes + 1
    post.likes = new_value
    post.save()
    return HttpResponseRedirect('/')
