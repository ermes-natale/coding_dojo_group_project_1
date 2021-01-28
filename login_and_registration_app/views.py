from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
from .models import User

def index(request):
    return render(request, 'index.html')

def process(request):
    if request.POST['which_form'] == 'register':
        errors = User.objects.validate(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/login")
        else:
            password = request.POST['password']
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], password = pw_hash)
            user = User.objects.filter(email = request.POST['email'])
            logged_user = user[0]
            request.session['userid'] = logged_user.id
            request.session['username'] = logged_user.name
            return redirect("/")
    
    if request.POST['which_form'] == 'login':
        user = User.objects.filter(email = request.POST['email'])
        if user:
            logged_user = user[0]
            request.session['userid'] = logged_user.id
            request.session['username'] = logged_user.first_name
            if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
                return redirect("/")

        messages.error(request, "Username or Password is incorrect")
        return redirect("/login")

def success(request):
    if 'userid' in request.session:
        context ={
            'user': User.objects.get(id=request.session['userid']),
        }
        return render(request, 'success.html', context)
    return redirect("/login")

def log_out(request):
    del request.session['userid']
    return redirect("/login")
