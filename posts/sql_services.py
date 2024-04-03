from django.shortcuts import redirect
from django.http.response import HttpResponsePermanentRedirect, HttpResponseRedirect

from .models import Posts
from .forms import PostForm


def save_post_form(request, to_redirect: str) -> HttpResponsePermanentRedirect | HttpResponseRedirect | bool:
    form = PostForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect(to_redirect)

    return False


def get_post_object(id_post: int) -> Posts | bool:
    post = Posts.objects.filter(id=id_post).first()
    if post:
        return post

    return False


def delete_post_object(id_post: int, to_redirect: str) -> HttpResponsePermanentRedirect | HttpResponseRedirect:
    Posts.objects.filter(id=id_post).delete()
    return redirect(to_redirect)
