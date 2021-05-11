from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreateUserForm
# Create your views here.
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Info
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

    resumes = request.user.info_set.all().filter()
    # resumes = reversed(list(resumes))
    context = {'resumes': resumes}
    return render(request, 'resume.html', context)


@login_required(login_url='login')
def create_resume(request):
    if request.method == "POST":
        profile_name = request.POST.get("profile_name")
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        phone = request.POST.get("phone")
        email = request.POST.get("email")

        dep = request.POST.get("dep")
        roll = request.POST.get("roll")
        github = request.POST.get("github")
        linkedin = request.POST.get("linkedin")
        portfolio = request.POST.get("portfolio")

        clg = request.POST.get("clg")
        clg_cg = request.POST.get("clg_cg")
        start_clg = request.POST.get("start_clg")
        end_clg = request.POST.get("end_clg")

        edu = request.POST.get("edu")
        edu_cg = request.POST.get("edu_cg")
        start_edu = request.POST.get("start_edu")
        end_edu = request.POST.get("end_edu")

        exp1 = request.POST.get("exp1")
        start_exp1 = request.POST.get("start_exp1")
        end_exp1 = request.POST.get("end_exp1")
        exp1_info = request.POST.get("exp1_info")

        exp2 = request.POST.get("exp2")
        start_exp2 = request.POST.get("start_exp2")
        end_exp2 = request.POST.get("end_exp2")
        exp2_info = request.POST.get("exp2_info")

        exp3 = request.POST.get("exp3")
        start_exp3 = request.POST.get("start_exp3")
        end_exp3 = request.POST.get("end_exp3")
        exp3_info = request.POST.get("exp3_info")

        pj1 = request.POST.get("pj1")
        start_pg1 = request.POST.get("start_pg1")
        end_pg1 = request.POST.get("end_pg1")
        pg1_info = request.POST.get("pg1_info")

        pj2 = request.POST.get("pj2")
        start_pg2 = request.POST.get("start_pg2")
        end_pg2 = request.POST.get("end_pg2")
        pg2_info = request.POST.get("pg2_info")

        pj3 = request.POST.get("pj3")
        start_pg3 = request.POST.get("start_pg3")
        end_pg3 = request.POST.get("end_pg3")
        pg3_info = request.POST.get("pg3_info")

        Achievments = request.POST.get("Achievments")
        Skills = request.POST.get("Skills")
        Por = request.POST.get("Por")
        Hobbies = request.POST.get("Hobbies")

        user = request.user

        if profile_name != "" and firstname != "" and phone != "" and email != "":
            new = Info(user=user, profile_name=profile_name, firstname=firstname, lastname=lastname, phone=phone,
                       email=email, dep=dep, roll=roll, github=github, linkedin=linkedin, portfolio=portfolio,
                       clg=clg, clg_cg=clg_cg, start_clg=start_clg, end_clg=end_clg, edu=edu, edu_cg=edu_cg, start_edu=start_edu,
                       end_edu=end_edu, exp1=exp1, start_exp1=start_exp1, end_exp1=end_exp1, exp2=exp2, start_exp2=start_exp2,
                       end_exp2=end_exp2, exp3=exp3, start_exp3=start_exp3, end_exp3=end_exp3, pj1=pj1,
                       start_pg1=start_pg1, end_pg1=end_pg1, pj2=pj2, start_pg2=start_pg2, end_pg2=end_pg2, pj3=pj3,
                       pg3_info=pg3_info, pg2_info=pg2_info, pg1_info=pg1_info, exp1_info=exp1_info, exp2_info=exp2_info, exp3_info=exp3_info,
                       start_pg3=start_pg3, end_pg3=end_pg3, Achievments=Achievments, Skills=Skills, Por=Por, Hobbies=Hobbies)
            new.save()
            return redirect('resume')
        else:
            messages.info(request, 'Enter all the Important Details')

    context = {}
    return render(request, 'create_resume.html', context)


@login_required(login_url='login')
def update_resume(request, pk):
    profile = Info.objects.get(id=pk)
    if request.method == "POST":
        profile_name = request.POST.get("profile_name")
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        phone = request.POST.get("phone")
        email = request.POST.get("email")

        dep = request.POST.get("dep")
        roll = request.POST.get("roll")
        github = request.POST.get("github")
        linkedin = request.POST.get("linkedin")
        portfolio = request.POST.get("portfolio")

        clg = request.POST.get("clg")
        clg_cg = request.POST.get("clg_cg")
        start_clg = request.POST.get("start_clg")
        end_clg = request.POST.get("end_clg")

        edu = request.POST.get("edu")
        edu_cg = request.POST.get("edu_cg")
        start_edu = request.POST.get("start_edu")
        end_edu = request.POST.get("end_edu")

        exp1 = request.POST.get("exp1")
        start_exp1 = request.POST.get("start_exp1")
        end_exp1 = request.POST.get("end_exp1")
        exp1_info = request.POST.get("exp1_info")

        exp2 = request.POST.get("exp2")
        start_exp2 = request.POST.get("start_exp2")
        end_exp2 = request.POST.get("end_exp2")
        exp2_info = request.POST.get("exp2_info")

        exp3 = request.POST.get("exp3")
        start_exp3 = request.POST.get("start_exp3")
        end_exp3 = request.POST.get("end_exp3")
        exp3_info = request.POST.get("exp3_info")

        pj1 = request.POST.get("pj1")
        start_pg1 = request.POST.get("start_pg1")
        end_pg1 = request.POST.get("end_pg1")
        pg1_info = request.POST.get("pg1_info")

        pj2 = request.POST.get("pj2")
        start_pg2 = request.POST.get("start_pg2")
        end_pg2 = request.POST.get("end_pg2")
        pg2_info = request.POST.get("pg2_info")

        pj3 = request.POST.get("pj3")
        start_pg3 = request.POST.get("start_pg3")
        end_pg3 = request.POST.get("end_pg3")
        pg3_info = request.POST.get("pg3_info")

        Achievments = request.POST.get("Achievments")
        Skills = request.POST.get("Skills")
        Por = request.POST.get("Por")
        Hobbies = request.POST.get("Hobbies")

        user = request.user

        new = Info(id=pk, user=user, profile_name=profile_name, firstname=firstname, lastname=lastname, phone=phone,
                   email=email, dep=dep, roll=roll, github=github, linkedin=linkedin, portfolio=portfolio,
                   clg=clg, clg_cg=clg_cg, start_clg=start_clg, end_clg=end_clg, edu=edu, edu_cg=edu_cg, start_edu=start_edu,
                   end_edu=end_edu, exp1=exp1, start_exp1=start_exp1, end_exp1=end_exp1, exp2=exp2, start_exp2=start_exp2,
                   end_exp2=end_exp2, exp3=exp3, start_exp3=start_exp3, end_exp3=end_exp3, pj1=pj1,
                   start_pg1=start_pg1, end_pg1=end_pg1, pj2=pj2, start_pg2=start_pg2, end_pg2=end_pg2, pj3=pj3,
                   pg3_info=pg3_info, pg2_info=pg2_info, pg1_info=pg1_info, exp1_info=exp1_info, exp2_info=exp2_info, exp3_info=exp3_info,
                   start_pg3=start_pg3, end_pg3=end_pg3, Achievments=Achievments, Skills=Skills, Por=Por, Hobbies=Hobbies)
        new.save()
        return redirect('resume')

    context = {'profile': profile}
    return render(request, 'create_resume.html', context)


@login_required(login_url='login')
def delete_resume(request, pk):
    resume = Info.objects.get(id=pk)
    if request.method == "POST":
        resume.delete()
        return redirect('resume')

    context = {"resume": resume}
    return render(request, 'delete.html', context)


@login_required(login_url='login')
def choose_resume(request):
    resumes = request.user.info_set.all()
    context = {'resumes': resumes}
    return render(request, 'choose_resume.html', context)


@login_required(login_url='login')
def choose_template(request, pk):
    context = {"id": pk}
    return render(request, 'choose_template.html', context)


@login_required(login_url='login')
def view_template1(request, pk):
    resume = Info.objects.get(id=pk)
    context = {"resume": resume}
    return render(request, 'kgp_template.html', context)

@login_required(login_url='login')
def view_template2(request, pk):
    resume = Info.objects.get(id=pk)
    context = {"resume": resume}
    return render(request, 'template1.html', context)