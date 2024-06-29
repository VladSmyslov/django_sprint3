from django.urls import path
from blog.views import index, post_detail, category_posts


app_name = 'blog'

urlpatterns = [
    path('', index, name='index'),
    path('<int:id>/', post_detail, name='post_detail'),
    path('<slug:category_slug>/', category_posts, name='category_posts'),
]
