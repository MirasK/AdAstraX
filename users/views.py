from django.shortcuts import render, redirect
from .forms import UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required
def profile(request):
    if request.method == 'POST':
        uform = UserUpdateForm(request.POST, instance=request.user)
        pform = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if uform.is_valid() and pform.is_valid():
            uform.save()
            pform.save()
            messages.success(request, f'Account has been updated.')
            return redirect('profile')
    else:
        uform = UserUpdateForm(instance=request.user)
        pform = ProfileUpdateForm(instance=request.user.profile)

    return render(request, 'users/profile.html', {'uform': uform, 'pform': pform})



@login_required
def SearchView(request):
    if request.method == 'POST':
        query = request.POST.get('search')
        print(query)
        results = User.objects.filter(username__contains=query)
        context = {
            'results':results
        }
        return render(request, 'users/search_result.html', context)
