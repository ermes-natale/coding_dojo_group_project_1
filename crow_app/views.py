from django.shortcuts import render, redirect
from login_and_registration_app.models import User

def index(request):
    if 'username' in request.session:
        context ={
            'user': request.session['username'],
        }
        return render(request, 'success.html', context)
    return redirect("/login")
# Create your views here.
