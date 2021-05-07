from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreateUserForm
# Create your views here.
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib.auth.models import User

def register(request):
    if request.user.is_authenticated:
        return redirect('resume')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(
                    request, 'Account was created for ' + username)
                return redirect('login')

    context = {'form': form}
    return render(request, 'Register.html', context)


def loginPage(request):

    if request.user.is_authenticated:
        return redirect('resume')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('resume')
            else:
                messages.info(request, 'Username Or password is incorrect')

    context = {}
    return render(request, 'Login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def resume(request):

    resumes=request.user.profile_set.all().filter()
    context = {'resumes':resumes}
    return render(request, 'index.html', context)


@login_required(login_url='login')
def create_resume_1(request):
    if request.method == "POST":
        profile_name=request.POST.get("profile_name")
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        address = request.POST.get("address")
        city = request.POST.get("city")
        code = request.POST.get("code")
        other_info = request.POST.get("other_info")
        user=request.user

        profile = Profile(profile_name=profile_name,firstname=firstname, lastname=lastname, phone=phone,
                           email=email, address=address, city=city, code=code, other_info=other_info, user=user)
        profile.save()
        return redirect('create_resume_2')
        
    context = {}
    return render(request, 'create_resume_1.html', context)


@login_required(login_url='login')
def create_resume_2(request):
    context = {}
    return render(request, 'create_resume_2.html', context)
