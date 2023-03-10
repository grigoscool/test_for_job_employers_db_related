import json

import requests
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import Post
from .serializers import PostSerializer

url = 'https://jsonplaceholder.typicode.com/posts'


def show_posts(request):
    """ Send get request and write in db all new data """
    response = requests.get(url)
    if response.status_code == 200:
        posts = response.json()
        my_list = []
        for post in posts:
            my_list.append(post['title'])
            if not Post.objects.filter(pk=post['id']):
                Post.objects.create(userId=post['userId'], id=post['id'], title=post['title'], body=post['body'])

        context = {
            'posts': my_list,
        }

        return render(request, 'api/api_posts.html', context)
    return render(request, 'api/api_posts.html')


def send_posts(request):
    """ Send post request and write received post in db if it is new """
    post = Post.objects.values('id', 'body').get(pk=1)
    serialize = PostSerializer(post)
    send = requests.post(url, data=serialize.data)
    if send.status_code == 201:
        response = send.json()

        if not Post.objects.filter(pk=response['id']):
            add_post = Post.objects.create(id=response['id'], body=response['body'])
            context = {
                'new_post': add_post,
            }
        else:
            context = {
                'new_post': response,
            }
        return render(request, 'api/api_send_posts.html', context)
    return render(request, 'api/api_send_posts.html')


def send_my_fio(request):
    """ Send post request with my fio and the list of results from my tests """
    posts = Post.objects.values('title').all()
    my_list = []
    for post in posts:
        my_list.append(post['title'])

    fio = {
        "name": "Sergey Grigorev",
        "repo_url": "https://github.com/grigoscool/test_for_work.git",
        "result": my_list
    }

    data = json.dumps(fio)
    response = requests.post(url, data=fio)

    if 200 <= response.status_code <= 299:

        context = {
            'fio': data,
        }
        return render(request, 'api/send_api_fio.html', context)
    else:
        return render(request, 'api/send_api_fio.html')


class PostViewApiLIst(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
