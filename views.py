from django.shortcuts import render
from .models import Blog

# Create your views here.
def home_view(request):
    blogpost = Blog.objects.all()
    context = {'blogposts':blogpost}
    return render(request, 'index.html', context)
