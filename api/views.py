from django.shortcuts import render
import requests
import json

from psycopg2 import IntegrityError

from .models import Post

def show_users(request):
    posts = requests.get('https://jsonplaceholder.typicode.com/posts').json()
    my_list = []
    for post in posts:
        my_list.append(post['title'])
        if not Post.objects.filter(pk=post['id']):
            Post.objects.create(userId=post['userId'], id=post['id'], title=post['title'], body=post['body'])

    context = {
        'posts': my_list,
    }

    return render(request, 'api/api_users.html', context)