from django.urls import path
from blog import views

urlpatterns = [
                path('post/', views.PostListView.as_view(), name='post_list'),
                path('post/new/', views.PostCreateView.as_view(), name='post_new'),
                path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
                path('about/', views.AboutView.as_view(),name='about')
]