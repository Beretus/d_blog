from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='base_generic'),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='post-detail'),
]

