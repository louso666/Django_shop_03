from django.shortcuts import render, get_object_or_404
from .models import BlogPost, BlogCategory, BlogTag

def post_list(request):
    posts = BlogPost.objects.filter(status='published').order_by('-date_published')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug, status='published')
    return render(request, 'blog/post_detail.html', {'post': post})

def category_posts(request, category_slug):
    category = get_object_or_404(BlogCategory, slug=category_slug)
    posts = BlogPost.objects.filter(category=category, status='published').order_by('-date_published')
    return render(request, 'blog/post_list.html', {'posts': posts, 'category': category})

def tag_posts(request, tag_slug):
    tag = get_object_or_404(BlogTag, slug=tag_slug)
    posts = BlogPost.objects.filter(tags=tag, status='published').order_by('-date_published')
    return render(request, 'blog/post_list.html', {'posts': posts, 'tag': tag})
