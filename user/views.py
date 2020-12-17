from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from rest_framework import viewsets, generics

from .models import User
from .serializers import UserSerializer, UserListSerializer

    

# Create your views here.
def userById(request, id):
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        raise Http404("User does not exist")
    return HttpResponse(f"usuario {user.name} criado em: {user.created_at}")


def users(request):
    users = User.objects.order_by('created_at')
    template = loader.get_template('users/index.html')
    context = {'users': users,}
    return HttpResponse(template.render(context, request))


class UserViewSet(viewsets.ModelViewSet):    
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ListUser(generics.ListAPIView):
    def get_queryset(self):
        queryset = User.objects.all()
        return queryset
    serializer_class = UserListSerializer
