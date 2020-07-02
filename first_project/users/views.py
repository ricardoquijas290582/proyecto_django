from django.shortcuts import render
from django.contrib.auth.models import User

def GetUsers(request):
    users = Users.objects.filter(is_superuser=False)
    context = {
        'users': users
    }
    return render(request, )
# Create your views here.
