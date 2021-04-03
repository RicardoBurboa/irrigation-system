#para renderear el html y redireccionar
from django.shortcuts import render, redirect
#Crea un form directo del framework Django
#from django.contrib.auth.forms import UserCreationForm
#Para saber si tengo un error
from django.contrib import messages
#para que no puedas entrar a /profile si no has iniciado sesión
from django.contrib.auth.decorators import login_required
#Clase de forms que hereda al form genérico de Django
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

def register(request):
    #FORM
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            #para guardar el usuario. importante que el form.save() esté primero
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'¡Tu cuenta ha sido creada, {username}! Ahora puedes iniciar sesión.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        #los parámetros sirven como placeholder dentro del form
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid() :
            u_form.save()
            p_form.save()
            messages.success(request, f'¡Tu cuenta ha sido actualizada!')
            return redirect('profile')
    else:
        #los parámetros sirven como placeholder dentro del form
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)
