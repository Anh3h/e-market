from django.shortcuts import render, redirect

from .forms import SignUpForm


def home(request):
    return render(request, 'core/home.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.telephone = form.cleaned_data.get('telephone')
            user.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'core/auth/signup.html', {'form': form})
