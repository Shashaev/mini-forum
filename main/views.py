from django.shortcuts import render
from posts.models import Posts


def index(request):
    all_posts = Posts.objects.all().order_by('-id')

    context = {'posts': all_posts}

    return render(request=request, template_name='main/index.html', context=context)
