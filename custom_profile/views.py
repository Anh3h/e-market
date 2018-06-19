from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


@login_required
def profile(request):
    if request.method == 'POST':
        request.user.first_name = request.POST.get("first_name", "")
        request.user.last_name = request.POST.get("last_name", "")
        request.user.profile.telephone = request.POST.get("telephone", "")
        request.user.profile.location = request.POST.get("location", "")
        request.user.save()
        return redirect('home')
    return render(request, 'core/auth/profile.html', {'user': request.user})


@login_required
def password(request):
    error = ""
    if request.method == 'POST':
        password1 = request.POST.get("password1", "").strip()
        password2 = request.POST.get("password2", "").strip()
        if password1 == password2:
            if len(password1) > 8:
                request.user.set_password(password1)
                request.user.save()
                return redirect('login')
            error = "The password is too short, it should be at least 8 characters long"
        else:
            error = "The two password fields didn't match."
    return render(request, 'core/auth/password.html', {'error': error})
