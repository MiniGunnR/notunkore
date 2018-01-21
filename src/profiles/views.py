from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect

from .models import Profile


def redirect_to_profile(request):
    return HttpResponseRedirect(reverse('profiles:profile', args=[str(request.user.id)]))


def profile(request, pk):
    obj = Profile.objects.get(user_id=pk)

    context = {
        "profile": obj,
    }
    return render(request, "profiles/profile.html", context)
