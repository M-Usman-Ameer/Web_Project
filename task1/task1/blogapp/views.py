from django.shortcuts import render,get_object_or_404
from blogapp.models import Postblog
def home(request):
    posts = Postblog.objects.all()
    return render(request,'home.html',{'posts':posts})

def post(request,slug):
    posts = get_object_or_404(Postblog,slug=slug)
    return render(request,'post.html',{'posts':posts})