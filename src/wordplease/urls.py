"""wordplease URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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


from blogging.views import home, CreatePostView, blogs, MyBlogView,post_detail
from blogging.api import PostListAPI, PostDetailAPI

from users.api import UsersListAPI, UserDetailAPI

from users.views import logout, LoginView, SignupView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', LoginView.as_view(), name="login_page"),
    path('signup', SignupView.as_view(), name= "signup_page"),
    path('logout', logout, name="logout_page"),

    #<a href="{% url "blogs_list_page" %}">Blogs List </a> |
    #        <a href="{% url "myblogs_page" %}">Blogs List </a> |
    #        <a href="{% url "create_post_page" %}">Blogs List </a> |

    #path('pelis/crear', CreateMovieView.as_view(), name="create_movie_page"),
    #path('pelis/<int:pk>', movie_detail, name="movie_detail_page"),
    #path('pelis/', MyMoviesView.as_view(), name="my_movies_page"),
    path('blogs/<str:username>/<int:pk>',post_detail ,name="posts_detail_page"),
    path('blogs/<str:username>',MyBlogView.as_view() ,name="myblogs_page"),
    path('blogs/', blogs, name='blogs_list_page'),
    path('new_post', CreatePostView.as_view(), name="create_post_page"),
    path('', home, name="home_page"),

    # API REST
    #path('api/1.0/hello/', HelloWorld.as_view(), name="api_hello_world"),
    path('api/1.0/users/<int:pk>', UserDetailAPI.as_view(), name="api_user_detail"),
    path('api/1.0/users/', UsersListAPI.as_view(), name="api_users_list"),

    path('api/1.0/movies/<int:pk>', PostDetailAPI.as_view(), name="api_post_detail"),
    path('api/1.0/movies/', PostListAPI.as_view(), name="api_post_list"),

]
