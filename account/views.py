from django.shortcuts import render
from django.http import HttpResponse
from account.forms import RegistrationForm


def register(request):
    if request.user.is_authenticated:
        return HttpResponse('You are authenticated!')
    else:
        form = RegistrationForm()
        if request.method == 'post' or request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponse('Your account has been created!')

        context = {
            'form': form
        }
    return render(request, 'register.html', context)
