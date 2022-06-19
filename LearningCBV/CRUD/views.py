from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from .models import Blog
from .forms import BlogAddForm
# Create your views here.
class HomePage(ListView):
    model = Blog
    queryset = Blog.objects.filter(status='draft').all()
    template_name = 'homepage.html'
    context_object_name = 'blogs'

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'detailView.html'
    context_object_name = 'postDetail'

class TemplateRender(TemplateView):
    template_name = "homepage.html"

    def get_context_data(self, **kwargs):
        return {
            'blogDraft': Blog.objects.filter(status='draft'),
            'blogPublished': Blog.objects.filter(status='published')
        }

class ModifyBlog(ListView):
    model = Blog
    template_name = 'modify.html'
    context_object_name = 'modify'

class AddBlog(CreateView):
    model = Blog
    form_class = BlogAddForm
    template_name = 'addBlog.html'
    # success_url = reverse_lazy('detail_view')
    success_url = '/'

class UpdateBlog(UpdateView):
    model = Blog
    form_class = BlogAddForm
    pk_url_kwarg = 'pk'
    template_name = 'updateBlog.html'
    success_url = '/'

class DeleteBlog(DeleteView):
    model = Blog
    pk_url_kwarg = 'pk'
    template_name = 'deleteBlog.html'
    success_url = '/'