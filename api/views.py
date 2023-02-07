from django.shortcuts import render
import requests
import json

def show_users(request):
    response = requests.get('https://jsonplaceholder.typicode.com/users').json()
    context = {
        'users': response,
    }
    return render(request, 'api/api_users.html', context)