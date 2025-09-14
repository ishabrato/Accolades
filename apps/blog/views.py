from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post

def post_list(request):
    return HttpResponse("I am blog")

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return HttpResponse(f"I am blog post: {post.title}")