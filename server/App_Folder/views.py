from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .api.arxiv.arxiv_search import get_arxiv_data

# Create your views here.
class Arxiv_Search(APIView):
    def get(self, request):
        # return Response("OK", status=status.HTTP_200_OK)
        return Response(get_arxiv_data('LLM cat:cs.CL'))
    
    def post(self, request, *args, **kwargs):
        search_word = request.data
        return Response(get_arxiv_data(search_word['search']))