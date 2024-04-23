from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response

from apps.api.serializer import DecksSerializer, GroupSerializer, UserSerializer
from apps.api.models import Decks


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = [permissions.AllowAny]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.AllowAny]

class HandleDecks(APIView):
    def get(self, request):
        tasks = Decks.objects.all()
        serializer = DecksSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DecksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)