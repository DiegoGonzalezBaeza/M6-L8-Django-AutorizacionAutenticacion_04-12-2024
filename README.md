# Django Authentication & Authorization Project

Este proyecto implementa un sistema de autenticación y autorización utilizando el framework Django. Se incluye funcionalidad para login y logout, junto con medidas de seguridad estándar de Django.

## Características

- **Autenticación de usuarios:**
  - Inicio de sesión (`/login/`).
  - Cierre de sesión (`/logout/`) con redirección a `/home/`.

- **Seguridad:**
  - Protección CSRF integrada.
  - Middleware para autenticación y gestión de sesiones.

- **Redirección:**
  - Redirección después de login y logout configurada en `settings.py`:
    - `LOGIN_REDIRECT_URL = '/'`
    - `LOGOUT_REDIRECT_URL = '/home/'`

- **Interfaz de usuario:**
  - Uso de Bootstrap para un diseño moderno y responsivo.
  - Formularios estilizados y fáciles de usar.

## Requisitos

- Python 3.6 o superior.
- Django 4.0 o superior.

## Instalación

1. **Clonar el repositorio:**
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd auth_project
   ```

2. **Crear un entorno virtual y activarlo:**
   ```bash
   python -m venv env
   source env/bin/activate  # En Windows: env\Scripts\activate
   ```

3. **Instalar dependencias:**
   ```bash
   pip install django
   ```

4. **Aplicar migraciones:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Crear un superusuario (opcional):**
   ```bash
   python manage.py createsuperuser
   ```

6. **Iniciar el servidor:**
   ```bash
   python manage.py runserver
   ```

## Estructura del Proyecto

```
auth_project/
├── auth_app/
│   ├── templates/
│   │   ├── auth_app/
│   │   │   ├── login.html
│   │   │   ├── logout.html
│   │   │   ├── index.html
│   ├── views.py
│   ├── urls.py
│   ├── models.py
├── auth_project/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
```

## Rutas Principales

| Ruta        | Descripción                                   |
|-------------|-----------------------------------------------|
| `/login/`   | Página de inicio de sesión.                   |
| `/logout/`  | Cierra la sesión y redirige a `/home/`.       |
| `/home/`    | Página de inicio después de cerrar sesión.    |
| `/`         | Página principal con opciones para usuarios autenticados o no autenticados. |

## Código Clave

### Configuración en `settings.py`
```python
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/home/'
```

### URLs en `auth_app/urls.py`
```python
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='auth_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('home/', views.home, name='home'),
    path('', views.index, name='index'),
]
```

### Plantillas Clave

#### **`login.html`**
Formulario para iniciar sesión:
```html
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit" class="btn btn-primary w-100">Login</button>
</form>
```

#### **`logout.html`**
Página personalizada después del cierre de sesión:
```html
<h1 class="text-center">You have been logged out</h1>
<p class="text-center mt-3"><a href="{% url 'login' %}" class="btn btn-primary">Login Again</a></p>
```

#### **`index.html`**
Página principal:
```html
{% if user.is_authenticated %}
    <p class="text-center">Hello, {{ user.username }}!</p>
    <form method="post" action="{% url 'logout' %}">
        {% csrf_token %}
        <button type="submit" class="btn btn-danger">Logout</button>
    </form>
{% else %}
    <p class="text-center"><a href="{% url 'login' %}" class="btn btn-primary">Login</a></p>
{% endif %}
```

## Seguridad

El proyecto utiliza todas las medidas de seguridad proporcionadas por Django:
- **Protección CSRF:** Activa por defecto para prevenir ataques de falsificación de solicitudes.
- **Middleware de autenticación:** Gestiona sesiones de usuario de forma segura.
- **Contraseñas cifradas:** Gestionadas mediante el sistema de hashing de Django.

# Django Authentication & Authorization Project - Parte 2

En esta segunda versión del proyecto, hemos agregado la funcionalidad de **registro de usuarios** para complementar las características existentes de autenticación y autorización.

## Nuevas Características

- **Registro de usuarios:**
  - Formulario de registro con los campos `username`, `email`, `password1`, y `password2`.
  - Validación de datos del formulario integrada.
  - Redirección al login después de un registro exitoso.

- **Plantillas mejoradas:**
  - Nueva plantilla para registro (`register.html`).
  - Enlace al registro desde la página de login.

## Rutas Principales

| Ruta         | Descripción                                    |
|--------------|------------------------------------------------|
| `/login/`    | Página de inicio de sesión.                   |
| `/logout/`   | Cierra la sesión y redirige a `/home/`.        |
| `/register/` | Página de registro de nuevos usuarios.        |
| `/home/`     | Página de inicio después de cerrar sesión.     |
| `/`          | Página principal con opciones para usuarios autenticados o no autenticados. |

## Instalación

1. **Clonar el repositorio:**
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd auth_project
   ```

2. **Crear un entorno virtual y activarlo:**
   ```bash
   python -m venv env
   source env/bin/activate  # En Windows: env\Scripts\activate
   ```

3. **Instalar dependencias:**
   ```bash
   pip install django
   ```

4. **Aplicar migraciones:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Crear un superusuario (opcional):**
   ```bash
   python manage.py createsuperuser
   ```

6. **Iniciar el servidor:**
   ```bash
   python manage.py runserver
   ```

## Código Clave

### Formulario de Registro (`forms.py`)
```python
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].widget.attrs['class'] = 'form-control'
```

### Vista de Registro (`views.py`)
```python
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'auth_app/register.html', {'form': form})
```

### URLs (`urls.py`)
```python
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='auth_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home'),
    path('', views.index, name='index'),
]
```

### Plantilla de Registro (`register.html`)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Register</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-light">
    <div class="container mt-5">
        <h1 class="text-center mb-4">Register</h1>
        <div class="card p-4 shadow-sm">
            <form method="post">
                {% csrf_token %}
                {{ form.as_p }}
                <button type="submit" class="btn btn-primary w-100">Register</button>
            </form>
        </div>
        <p class="text-center mt-3">Already have an account? <a href="{% url 'login' %}">Login here</a></p>
    </div>
</body>
</html>
```

### Actualización en la Plantilla de Login (`login.html`)
```html
<p class="text-center mt-3">Don't have an account? <a href="{% url 'register' %}">Register here</a></p>
```

## Cómo Probar el Registro

1. Ve a la URL `/register/`.
2. Completa el formulario con los datos de un nuevo usuario.
3. Después de un registro exitoso, serás redirigido a `/login/`.
4. Inicia sesión con las credenciales recién creadas.

## Estructura del Proyecto

```
auth_project/
├── auth_app/
│   ├── templates/
│   │   ├── auth_app/
│   │   │   ├── login.html
│   │   │   ├── logout.html
│   │   │   ├── register.html
│   │   │   ├── index.html
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   ├── models.py
├── auth_project/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
```