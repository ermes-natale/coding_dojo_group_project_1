from django.shortcuts import render, redirect

def index(request):
    if 'username' in request.session:
        context ={
            'user': request.session['username'],
        }
        return render(request, 'success.html', context)
    return redirect("/login")
# Create your views here.
