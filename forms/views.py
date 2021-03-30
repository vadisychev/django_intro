from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import UserInfo
from .forms import NameForm
from django.utils import timezone


def registration_book(request):
    user_list = UserInfo.objects.all()
    context = {
        'user_list': user_list,
    }
    return render(request, 'forms/registration_book.html', context)


def input_info(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            new_user = UserInfo(
                first_name=form.cleaned_data.get('first_name'),
                last_name=form.cleaned_data.get('last_name'),
                user_email=form.cleaned_data.get('user_email'),
                registration_date=timezone.now()
                )
            new_user.save()
            return HttpResponseRedirect('')
    else:
        form = NameForm()
    return render(request, 'forms/input_info.html', {'form': form})
