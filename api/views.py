from django.shortcuts import render, redirect
import requests
import json

from psycopg2 import IntegrityError

from .models import Post

url = 'https://jsonplaceholder.typicode.com/posts'


def show_posts(request):
    posts = requests.get(url).json()
    my_list = []
    for post in posts:
        my_list.append(post['title'])
        if not Post.objects.filter(pk=post['id']):
            Post.objects.create(userId=post['userId'], id=post['id'], title=post['title'], body=post['body'])

    context = {
        'posts': my_list,
    }

    return render(request, 'api/api_posts.html', context)


def send_posts(request):
    post = Post.objects.values('id', 'body').get(pk=1)
    send = requests.post(url, data=post)
    resp = send.json()
    if not Post.objects.filter(pk=resp['id']):
        add_post = Post.objects.create(id=resp['id'], body=resp['body'])
        context = {
            'new_post': add_post,
        }
    context = {
        'new_post': resp,
    }
    return render(request, 'api/api_send_posts.html', context)