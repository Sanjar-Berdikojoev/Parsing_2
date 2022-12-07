from django.urls import path
from . import views

app_name = 'parse'

urlpatterns = [
    path('', views.ParserFormView.as_view(), name='parse_func'),
    path('parser_goods_info/', views.ParserView.as_view(), name='parse_view'),
]