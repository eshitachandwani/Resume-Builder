from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreateUserForm
# Create your views here.
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib.auth.models import User
from django.template import loader


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

    resumes = request.user.profile_set.all().filter()
    # resumes = reversed(list(resumes))
    context = {'resumes': resumes}
    return render(request, 'resume.html', context)


@login_required(login_url='login')
def create_resume_1(request):
    if request.method == "POST":
        profile_name = request.POST.get("profile_name")
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        address = request.POST.get("address")
        city = request.POST.get("city")
        code = request.POST.get("code")
        other_info = request.POST.get("other_info")
        user = request.user

        if profile_name != "" and firstname != "" and phone != "" and email != "":
            profile = Profile(profile_name=profile_name, firstname=firstname, lastname=lastname, phone=phone,
                              email=email, address=address, city=city, code=code, other_info=other_info, user=user)
            profile.save()
            return redirect('resume')
        else:
            messages.info(request, 'Enter all the Important Details')

    context = {}
    return render(request, 'create_resume_1.html', context)


@login_required(login_url='login')
def update_resume(request, pk):
    profile = Profile.objects.get(id=pk)
    if request.method == "POST":
        profile_name = request.POST.get("profile_name")
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        address = request.POST.get("address")
        city = request.POST.get("city")
        code = request.POST.get("code")
        other_info = request.POST.get("other_info")
        user = request.user
        new = Profile(id=pk, profile_name=profile_name, firstname=firstname, lastname=lastname, phone=phone,
                      email=email, address=address, city=city, code=code, other_info=other_info, user=user)
        new.save()
        return redirect('resume')

    context = {'profile': profile}
    return render(request, 'create_resume_1.html', context)


@login_required(login_url='login')
def delete_resume(request, pk):
    resume = Profile.objects.get(id=pk)
    if request.method == "POST":
        resume.delete()
        return redirect('resume')

    context = {"resume": resume}
    return render(request, 'delete.html', context)


@login_required(login_url='login')
def choose_resume(request):
    resumes = request.user.profile_set.all()
    context = {'resumes': resumes}
    return render(request, 'choose_resume.html', context)


@login_required(login_url='login')
def choose_template(request, pk):
    context = {"id": pk}
    return render(request, 'choose_template.html', context)


@login_required(login_url='login')
def view_template1(request, pk):
    resume = Profile.objects.get(id=pk)
    context = {"resume": resume}
    return render(request, 'template1.html', context)


@login_required(login_url='login')
def print_template1(request, pk):
    resume = Profile.objects.get(id=pk)
    template = loader.get_template('template1.html')
    html = template.render({'resume': resume})

    options = {
        'encoding': 'UTF-8'
    }

    pdf = pdfkit.from_string(html, False, options)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachments'
    return response