from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic import ListView
from blogging.models import Post
from blogging.forms import PostForm


def hello_world(request):
    name = request.GET.get("name")
    if name is None:
        return HttpResponse("Hello world!")
    else:
        return HttpResponse("Hello " + name)


@login_required
def home(request):
    latest_post = Post.objects.all().order_by("-release_date")
    context = {'post': latest_post[:5]}
    return render(request, "home.html", context)

@login_required
def blogs(request):
    list_of_users = User.objects.all()
    context = {'users': list_of_users}
    return render(request, "blogs.html", context)

@login_required
def post_detail(request,username,pk):
    possible_post = Post.objects.filter(pk=pk).select_related(username)
    if len(possible_post) == 0:
        return render(request, "404.html", status=404)
    else:
        post = possible_post[0]
        context = {'post': post}
        return render(request, "post_detail.html", context)

class CreatePostView(LoginRequiredMixin, View):

    def get(self, request):
        form = PostForm()
        return render(request, "post_form.html", {'form': form})

    def post(self, request):
        post = Post()
        post.user = request.user
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            form = PostForm()
            url = reverse("post_detail_page", args=[post.pk])
            message = "Post created successfully! "
            message += '<a href="{0}">View</a>'.format(url)
            messages.success(request, message)
        return render(request, "post_form.html", {'form': form})

class MyBlogView(ListView):
      model = Post
      template_name = "blog_detail.html"

      def get_queryset(self):
        queryset = super(MyBlogView, self).get_queryset()
        return queryset.filter(user=self.request.user)
