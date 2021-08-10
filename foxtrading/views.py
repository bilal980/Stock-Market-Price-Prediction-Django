from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from acounts.models import CustomUser
from django.contrib.auth import authenticate, login, logout
from blog.models import Post
from django.contrib.auth.decorators import login_required

def foxLogin(request):
    try:
        if request.user.is_authenticated:
            return redirect('home/')
        return render(request, 'login.html')
    except:
        return HttpResponse("Server Error ....")

def foxSignup(request):
    try:
        return render(request, 'signup.html')
    except:
        return HttpResponse("Page Not Found ....")

@login_required
def foxHome(request):
    try:
        newpost = Post.objects.all().order_by('-time')[0:3]
        context = {'newpost': newpost, 'sbar': 'home'}
        return render(request, 'home.html', context)
    except:
        return HttpResponse("Sorry! Server Error ....")

@login_required(login_url='/')
def about(request):
    try:
        return render(request, 'about.html', {'sbar': 'about'})
    except:
        return HttpResponse("Page Not Found ....")


def foxLogout(request):
    try:
        logout(request)
        messages.success(request, 'Logout successfully')
        return redirect('/')
    except:
        return HttpResponse("Page Not Found ....")


def handleLogin(request):
    try:
        if request.method == 'POST':
            loginuseremail = request.POST['loginemail']
            loginpassword = request.POST['loginpassword']
            user = authenticate(email=loginuseremail, password=loginpassword)
            if user is not None:
                login(request, user)
                return redirect('/home')
            else:
                messages.error(request, 'Invalid Credentials')
                return redirect('/')
        return render(request, 'login.html')
    except:
        return HttpResponse("Page Not Found ....")

def handleSignup(request):
    if request.method == 'POST':
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        if pass1 != pass2:
            messages.error(request, 'Password do not match')
            return redirect('/signup')
        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, 'Email Alredy registered!')
            return redirect("/")
        myuser = CustomUser.objects.create_user(
            email=email, password=pass2)
        messages.success(request, "Please log in to continue!")
        return redirect('/')

@login_required(login_url='/')
def change_password(request):
    path_red = request.POST.get('back', '/')
    if request.user.is_authenticated:
        if request.method == 'POST':
            email = request.user.email
            new_password = request.POST['password1']
            new_password_confirm = request.POST['password2']
            if new_password != new_password_confirm:
                messages.error('Password do not Match!')
                return redirect(path_red)
            user = CustomUser.objects.get(email=email)
            user.set_password(new_password_confirm)
            user.save()
            messages.success(request, 'Password change successfully!')
            messages.warning(request, 'Please Login to Contnue...')
            return redirect(path_red)
        return render(request, 'change_password.html', {'sbar': 'profile'})
