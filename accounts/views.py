from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .forms import ProfileForm


@login_required
def edit_profile(request):
    profile = request.user.profile

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('my_profile_view')
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'accounts/edit_profile.html', {'form': form})


@login_required
def personal_profile_detail(request):
    return render(
        request,
        'accounts/profile_detail.html',
        {
            'profile': request.user.profile
        }
    )


@login_required
def other_profile_detail(request, username):
    User = get_user_model()
    user = get_object_or_404(User, username=username)
    return render(
        request,
        'accounts/profile_detail.html',
        {
            'profile': user.profile  # type: ignore
        }
    )
