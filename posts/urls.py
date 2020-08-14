from django.urls import path

from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.ListPosts.as_view(), name='all'),
    path('by/<username>/', views.UserPosts.as_view(), name='for_user'),
    path('new/', views.CreatePost.as_view(), name='create'),
    path('by/<username>/<int:pk>/', views.SinglePost.as_view(), name='single'),
    path('delete/<int:pk>/', views.DetailView.as_view(), name='delete')
]
