from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

@login_required
def index(request):
    return render(request, 'auth_app/index.html')

def home(request):
    return render(request, 'auth_app/home.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el nuevo usuario
            return redirect('login')  # Redirige al login después de registrar
    else:
        form = UserCreationForm()
    return render(request, 'auth_app/register.html', {'form': form})