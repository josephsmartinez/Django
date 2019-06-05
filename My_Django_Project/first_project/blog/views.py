from django.shortcuts import render
from django.http import HttpResponse


posts = [
    {
        'author': 'JohnD',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_post': 'August 27, 2019'
    }, 
    {
        'author': 'JaneD',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'date_post': 'August 28, 2019'
    }, 
]



# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About Page'})
