from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm
from django.contrib.auth.models import User

# Create your views here.

@login_required
def index(request):
    users = User.objects.all()
    return render(request, 'auth_app/index.html', {'users': users})

def home(request):
    return render(request, 'auth_app/home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirigir al login después del registro
    else:
        form = UserRegistrationForm()
    return render(request, 'auth_app/register.html', {'form': form})