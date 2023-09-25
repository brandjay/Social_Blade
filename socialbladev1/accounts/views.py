

# appname/views.py
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page or any other page you want
            return redirect('/admin')
        else:
            # Handle login failure, e.g., display an error message
            error_message = "Invalid login credentials. Please try again."
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'accounts/login.html')

