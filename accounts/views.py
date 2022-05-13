from django.contrib.auth import authenticate, login, logout
from resume.models import UserDetails
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from.forms import CreateUserForm


# TODO ask if user wants to register as User or HiringAgency
def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account is created for '+user)

            # for accessing which user is logged in, used it used multiple times
            request.session['uname'] = form.cleaned_data.get('username')

            return redirect('login')

    context = {'form': form}

    return render(request, 'register.html', context)


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            request.session['uname'] = username
            curr_user = UserDetails(u_id=User.objects.get(
                username=request.session['uname']), email_add=User.objects.get(username=request.session['uname']).email)
            curr_user.save()
            return redirect('profile_details')
        else:
            messages.info(request, 'invalid credentials')
    context = {}
    return render(request, 'login.html', context)


def home(request):
    return render(request, 'home.html')


def logoutUser(request):
    logout(request)
    return redirect('login')
