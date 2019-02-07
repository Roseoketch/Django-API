from django.urls import path
from django.conf.urls import url

from .views import ArticleView

app_name = "APIs"

urlpatterns = [
    path('API/', ArticleView.as_view()),
    path('API/<int:pk>', ArticleView.as_view())

]
