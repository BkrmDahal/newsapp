from django.shortcuts import render
from django.http import HttpResponse

from .models import Stories
app_name = 'blog'

# Create your views here.
def index(request):
    posts = Stories.objects.filter(pub_date__isnull=False).order_by('pub_date')
    return render(request, 'blog/index.html', {'posts': posts})
