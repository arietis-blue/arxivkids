from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class Arxiv_Search(APIView):
    def get(self, request):
        return Response("OK", status=status.HTTP_200_OK)