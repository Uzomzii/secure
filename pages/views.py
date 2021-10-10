from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
)
from .models import Post


class HomePageView(TemplateView):
    template_name = 'index.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'


class ServicePageView(TemplateView):
    template_name = 'service.html'


class ContactPageView(TemplateView):
    template_name = 'contact.html'


class BlogPageView(ListView):
    model = Post
    template_name = 'blog.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
