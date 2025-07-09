from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')  # Admission number
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            try:
                role = user.profile.role
            except Exception:
                messages.error(request, "Profile not found for this account.")
                return render(request, 'users/login.html')

            if role == 'student':
                login(request, user)
                return redirect('core:student_dashboard')
            else:
                messages.error(request, "You are not authorized to access this system.")
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, 'users/login.html')



def logout_view(request):
    logout(request)
    return redirect('users:login')
