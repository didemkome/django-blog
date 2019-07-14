# pylint: disable=no-member
import datetime

from django.shortcuts import render
from django.http import HttpResponse
from django.forms import ModelForm

from django.urls import reverse_lazy
from django.contrib import messages

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from django.contrib.messages.views import SuccessMessageMixin
from .models import Post

class PostList(ListView):
    model = Post
    # template_name = 'post_list.html'
    queryset = Post.custom_objects.latest_posts(7)

class PostDetail(DetailView):
    model = Post
    # queryset = Post.custom_objects.active()

class PostCreate(SuccessMessageMixin, CreateView):
    model = Post
    fields = ['title', 'body']
    success_url = reverse_lazy('post-list')
    success_message = '%(title)s was created successfully'

class PostUpdate(SuccessMessageMixin, UpdateView):
    model = Post
    fields = ['title', 'body']
    success_url = reverse_lazy('post-list')
    success_message = '%(title)s was updated successfully'

class PostDelete(SuccessMessageMixin, DeleteView):
    model = Post
    fields = ['title', 'body']
    success_url = reverse_lazy('post-list')
    success_message = '%(title)s was deleted successfully'

    def delete(self, request, *args, **kwargs):
        deleted_post = self.get_object()
        messages.success(self.request, self.success_message % deleted_post.__dict__)
        return super().delete(request, *args, **kwargs)


def index_view(request):
    return HttpResponse('Hello world')

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body']

def model_form_view(request):
    html_template = 'blog/model_form.html'
    result = ''
    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            new_post = form.save()
            result = 'New post saved as {new_post_id}'.format(new_post_id=new_post.index())
    else:
        form = PostForm()
    params = {
        'form': form,
        'result': result,
    }
    return render(
        request,
        html_template,
        params,
    )

# def show_detail(request, pk):
#     html_template = 'blog/post_detail.html'
#     params = {
#         'post' : Post.objects.get(pk=pk),
#     }
#     return render(request, html_template, params)

# def list_posts(request):
#     html_template = 'index.html'
#     params = {
#         'POSTS' : Post.custom_objects.latest_posts(),
#         'NOW' : datetime.datetime.now(),
#         'TEST_VAL': 'vigo'
#     }
#     return render(request, html_template, params)


