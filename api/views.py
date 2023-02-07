from django.shortcuts import render
import requests
import json

def show_users(request):
    response = requests.get('https://jsonplaceholder.typicode.com/posts').json()
    context = {
        'posts': response,
    }
    return render(request, 'api/api_users.html', context)