
from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages


def home(request):
    return render(request, 'authentication/index.html')

def signin(request):
    return render(request, "authentication/signin.html")

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        sdt = request.POST['sdt']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        myuser = User.objects.create(username,email,sdt,pass1,pass2)

        myuser.save()

        messages.success(request, "Đăng ký thành công")

        return redirect('signin')




    return render(request, "authentication/signup.html")

def forgotpass(request):
    return render(request, "authentication/forgotpass.html")