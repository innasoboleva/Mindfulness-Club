from django.contrib.auth.models import User
# from django.shortcuts import render
from rest_framework.decorators import api_view
# from rest_framework.response import Response
from django.http import JsonResponse
import json

@api_view(['GET'])
def index(request):
    data = {
        'page': 1,
        'status': 'success'
    }
    return JsonResponse(data)


@api_view(['POST'])
def create_user(request):

    if request.body:
        # Decoding the JSON data
        data = json.loads(request.body)
        username = data.get('username')
        first_name = data.get('firstName')
        last_name = data.get('lastName')
        email = data.get('email')
        password = data.get('password')
        # creating new user
        if username and email and password:
            new_user = User.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
            new_user.save()
            return JsonResponse({'status': 'success'})
    
    return JsonResponse({'status': 'error'})
   