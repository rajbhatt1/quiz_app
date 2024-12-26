
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import SignupForm, LoginForm ,admin_SignupForm
from .models import User

# Create your views here.
@login_required
def index(request):
    if request.user.is_authenticated and request.user.is_staff:
        queryset = User.objects.all()
        context = {
            'queryset': queryset
        }
        return render(request,'admin.html', context)
    else:
        user = request.user
        id = user.id
        fullname = user.fullname
        email = user.email
        context = {
            'id': id,
            'fullname': fullname,
            'email': email,
        }
        return render(request,'index.html', context)

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            role = form.cleaned_data['role']
            user=form.save()
            if role == 'admin':
                user.is_staff = True
                print('form:',form)
                user.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request,'signup.html',{'form':form})

def admin_signup(request):
    if request.method == 'POST':
        form = admin_SignupForm(request.POST)
        if form.is_valid():
            # role = form.cleaned_data['role']
            form.save()
            # if role == 'admin':
            #     user.is_staff = True
            #     print('form:',form)
            #     user.save()
            return redirect('admin_view')
    else:
        form = admin_SignupForm()
    return render(request,'admin_signup.html',{'form':form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request,email=email, password=password)
            if user:
                login(request, user)
                if request.user.is_authenticated and request.user.is_staff:
                    return redirect('admin_view')
                else:
                    return redirect('select_quiz')
    else:
        form = LoginForm()
    return render(request, 'login.html',{'form':form})

def user_logout(request):
    logout(request)
    return redirect('login')

def admin_view(request):
    if request.user.is_authenticated and request.user.is_staff:
        queryset = User.objects.all()
        context = {
            'queryset': queryset
        }
    return render(request, 'admin.html', context)