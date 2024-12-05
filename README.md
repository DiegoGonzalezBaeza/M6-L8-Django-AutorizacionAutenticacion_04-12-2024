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