from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.db import transaction

from profiles.models import Profile

from .forms import RegisterForm
from profiles.forms import ProfileForm


@transaction.atomic
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        profile_form = ProfileForm(request.POST)

        if form.is_valid() and profile_form.is_valid():
            form_data = form.cleaned_data
            profile_form_data = profile_form.cleaned_data

            user = User.objects.create_user(
                username    = form_data['username'],
                email       = form_data['email'],
                password    = form_data['password1'],
                first_name  = form_data['first_name'],
                last_name   = form_data['last_name']
            )

            Profile.objects.filter(user=user).update(
                dob             = profile_form_data['dob'],
                divorced        = profile_form_data['divorced'],
                divorced_number = profile_form_data['divorced_number'],
                children        = profile_form_data['children'],
                children_number = profile_form_data['children_number'],
                description     = profile_form_data['description']
            )

            return HttpResponseRedirect('/admin/')
    else:
        form = RegisterForm()
        profile_form = ProfileForm()
    context = {
        "form": form,
        "profile_form": profile_form,
    }
    return render(request, "core/register.html", context)
