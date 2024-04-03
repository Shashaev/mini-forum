from django.shortcuts import render
from .sql_services import save_post_form, get_post_object, delete_post_object
from .forms import PostForm


def get_post(request, id_post):
    post = get_post_object(id_post)

    context = {'post': post}

    return render(request=request, template_name='posts/post.html', context=context)


def create_post(request):
    if request.method == 'POST':
        return save_post_form(request, 'list_posts')

    form = PostForm()

    context = {'form': form}

    return render(request=request, template_name='posts/create_post.html', context=context)


def delete_post(request, id_post):
    if request.method == 'POST':
        return delete_post_object(id_post, 'list_posts')

    post = get_post_object(id_post)

    context = {'post': post}

    return render(request=request, template_name='posts/delete_post.html', context=context)


def update_post(request, id_post):
    if request.method == 'POST':
        save_post_form(request, 'list_posts')
        return delete_post_object(id_post, 'list_posts')

    post = get_post_object(id_post)

    form = PostForm(initial={'title': post.title, 'content': post.content})

    context = {'form': form, 'title_post': post.title}

    return render(request=request, template_name='posts/update_post.html', context=context)
