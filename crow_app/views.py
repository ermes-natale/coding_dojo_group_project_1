from django.shortcuts import render, redirect, HttpResonse
from login_and_registration_app.models import User

def index(request):
    if 'userid' in request.session:
        allposts = Post.objects.all().order_by("-created_at")
        post = allposts[0];
        context ={
            'user': User.objects.get(id=request.session['userid']),
            'post': post
        }
        return render(request, 'home.html', context)
    return redirect("/login")
# Create your views here.

def create_post(request):
    return HttpResonse("it works")

def archives(request):
    return HttpResonse("it works")

def updoot(request):
    return HttpResonse("this works, too")

def logout(request):
    request.session.clear()
    return redirect("/")
