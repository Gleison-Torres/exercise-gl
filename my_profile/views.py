from django.shortcuts import render


def my_profile_user(request):
    return render(request, 'my_profile.html')
