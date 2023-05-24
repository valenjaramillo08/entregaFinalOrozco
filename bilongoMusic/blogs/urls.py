from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='blogs'),
    path('<int:blogs_id>',views.blog, name='blog'),

]