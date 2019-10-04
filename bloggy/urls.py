"""bloggy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from accounts.views import UserRegistrationView
from django.contrib.auth.views import LoginView, LogoutView
from blog.views import NewBlogView, UpdateBlogView, NewBlogPostView, UpdateBlogPostView, BlogPostDetailsView, SharePostWithBlog, StopSharingPostWithBlog

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='base.html'), name='home'),
    path('new-user/', UserRegistrationView.as_view(), name='user_registration'),
    path('login/', LoginView.as_view(), {'template_name': 'login.>html'}, name='login'),
    path('logout/', LogoutView.as_view(), {'next_page': '/login/'}, name='logout'),
    path('blog/new/', NewBlogView.as_view(), name='new-blog'),
    path('blog/<int:pk>/update/', UpdateBlogView.as_view(), name='update-blog'),
    path('blog/post/new/', NewBlogPostView.as_view(), name='new-blog-post'),
    path('blog/post/<int:pk>/update/', UpdateBlogPostView.as_view(), name='update-blog-post'),
    path('blog/post/<int:pk>/', BlogPostDetailsView.as_view(), name='blog-post-details'),
    path('blog/post/<int:pk>/share/', SharePostWithBlog.as_view(), name='share-blog-post-with-blog'),
    path('blog/post/<int:pk>/share/to/<int:blog_pk>/', SharePostWithBlog.as_view(), name='share-post-with-blog'), 
    path('blog/post/<int:pk>/stop/share/to/<int:block_pk>/', StopSharingPostWithBlog.as_view(), name='stop-sharing-post-with-blog'),
]


