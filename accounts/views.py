from urllib.parse import urlencode

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.utils.http import url_has_allowed_host_and_scheme
from .forms import SignUpForm


def _get_login_redirect_url(request):
    redirect_to = request.POST.get("next") or request.GET.get("next", "")
    if redirect_to and url_has_allowed_host_and_scheme(
        url=redirect_to,
        allowed_hosts={request.get_host()},
        require_https=request.is_secure(),
    ):
        return redirect_to
    return None


# Login view
def login_user(request):
    if request.user.is_authenticated:
        return redirect(_get_login_redirect_url(request) or "index")

    if request.method == 'POST':
        u_name = request.POST['u_name']
        u_password = request.POST['u_password']

        user = authenticate(request, username=u_name, password=u_password)
        if user is not None:
            login(request, user)
            messages.success(request, 'User logged in successfully')
            return redirect(_get_login_redirect_url(request) or "index")
        else:
            messages.error(request, 'Invalid username or password')

    return render(
        request,
        'accounts/login.html',
        {"next": _get_login_redirect_url(request) or ""},
    )


# Signup view
def signup(request):
    if request.user.is_authenticated:
        return redirect(_get_login_redirect_url(request) or "index")

    form = SignUpForm(request.POST if request.method == 'POST' else None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Your account has been created. You can now log in.')
        redirect_to = _get_login_redirect_url(request)
        login_url = reverse("login")
        if redirect_to:
            login_url = f"{login_url}?{urlencode({'next': redirect_to})}"
        return redirect(login_url)

    return render(
        request,
        'accounts/signup.html',
        {"form": form, "next": _get_login_redirect_url(request) or ""},
    )


# Logout view
def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('login')
