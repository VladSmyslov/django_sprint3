import datetime

from django.shortcuts import get_list_or_404, get_object_or_404, render

from blog.models import Post


def index(request):
    template_name = 'blog/index.html'
    post_list = Post.objects.filter(
        pub_date__date__lt=datetime.date.today(),
        is_published__exact=True,
        category__is_published__exact=True
    ).order_by('-pub_date')[0:5]
    context = {
        'post_list': post_list
    }
    return render(request, template_name, context)


def post_detail(request, id):
    template_name = 'blog/detail.html'
    post = get_object_or_404(
        Post.objects.filter(
            pub_date__date__lt=datetime.date.today(),
            is_published__exact=True,
            category__is_published__exact=True
        ), pk=id
    )
    context = {'post': post}
    return render(request, template_name, context)


def category_posts(request, category_slug):
    template_name = 'blog/category.html'
    post_list = get_list_or_404(
        Post.objects.filter(
            is_published__exact=True,
            category__is_published__exact=True,
            category__slug__contains=category_slug,
            pub_date__date__lt=datetime.date.today(),
        )
    )
    context = {'post_list': post_list}
    return render(request, template_name, context)
