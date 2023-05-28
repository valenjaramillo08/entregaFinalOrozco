from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Blog

# Create your views here.
def index(request):
    blogs = Blog.objects.order_by('-fecha').filter(is_publish=True)
    paginator = Paginator(blogs,4)
    page = request.GET.get('page')
    paged_blogs = paginator.get_page(page)
    context = {'blogs':paged_blogs}

    return render(request, 'blogs/blogs.html', context)

def blog(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    context = {'blog': blog}
    return render(request, 'blogs/blog.html', context)