from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Article
from .serializers import ArticleSerializer
# Create your views here.

class ArticleView(APIView):
    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response({"articles": serializer.data})

    def post (self,request):
        article = request.data.get('article')

        serializer = ArticleSerializer(data=article)
        if serializer.is_valid(raise_exception=True):
            article_save = serializer.save()
        return Response({"success": "Article '{}' created successfully".format(article_save.title)})