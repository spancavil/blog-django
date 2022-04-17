from django.shortcuts import render, redirect

from .forms import SignupForm, UserAvatarForm, UserEditForm
from appblog.models import Avatar

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
@login_required
def my_profile(request):
    usuario = request.user
    avatar = Avatar.objects.filter(user=request.user).first()
    if request.method == "POST":
        user_edit_form = UserEditForm(request.POST)
        if user_edit_form.is_valid():
            data = user_edit_form.cleaned_data
            usuario.email = data["email"]
            usuario.first_name = data["first_name"]
            usuario.last_name = data["last_name"]
            usuario.password1 = data["password1"]
            usuario.password2 = data["password2"]
            usuario.save()
            return render(request, 'accountapp/myprofile.html', {"user_form": user_edit_form, "edit_success": True, "avatar": avatar})
        else:
            return render(request, 'accountapp/myprofile.html', {"user_form": user_edit_form, "avatar": avatar})
    else:
        user_edit_form = UserEditForm(initial={"email": usuario.email})
        user_avatar_form = UserAvatarForm()
        return render(request, 'accountapp/myprofile.html', {"user_form": user_edit_form, "user_avatar_form": user_avatar_form, "avatar": avatar})

@login_required
def avatar_upload(request):
    avatar = Avatar.objects.filter(user=request.user).first()
    user_avatar_form = UserAvatarForm()
    if request.method == "POST":
        image_form = UserAvatarForm(request.POST, request.FILES)
        print(request.POST)
        print(request.FILES)
        if image_form.is_valid():
            print("valid")
            #Preguntamos por avatar existentes
            existent_avatar = Avatar.objects.filter(user=request.user)
            if len(existent_avatar)>0:
                existent_avatar = existent_avatar[0]
                existent_avatar.image = image_form.cleaned_data["image"]
                existent_avatar.save()
                return render(request, 'accountapp/change_avatar.html', { "user_avatar_form": image_form, "edit_success": True, "avatar": existent_avatar})
            else:
                try:
                    usuario = User.objects.get(username=request.user)
                    print(usuario)
                    avatar = Avatar(user=usuario, image=image_form.cleaned_data["image"])
                    avatar.save()
                    return render(request, 'accountapp/change_avatar.html', { "user_avatar_form": image_form, "edit_success": True, "avatar": avatar})
                except Exception as e:
                    print(e)
                    return render(request, 'accountapp/change_avatar.html', { "user_avatar_form": image_form, "avatar": None})
        else:
            print("not valid")
            return render(request, 'accountapp/change_avatar.html', { "user_avatar_form": image_form, "avatar": avatar})
    else:
        return render(request, 'accountapp/change_avatar.html', { "user_avatar_form": user_avatar_form, "avatar": avatar})

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            print(usuario)
            form.save()
            return redirect("index")
        else:
            return render(request, "accountapp/signup.html", {"signup_form": form})
    else:
        form = SignupForm()
        return render(request, "accountapp/signup.html", {"signup_form": form})

def log_in(request):
    if request.method == "POST":
        form = AuthenticationForm()
        formulario = AuthenticationForm(request, data=request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            nombre_usuario = data.get("username")
            contrasenia = data.get("password")

            usuario = authenticate(username=nombre_usuario, password=contrasenia)

            if usuario:
                login(request, usuario)
                return redirect("index")
            else:
                return render(request, "accountapp/login.html", {"error": "Bad username/password", "login_form": form})
        else:
            return render(request, "accountapp/login.html", {"error": "Enter a valid username/password", "login_form": form})
    else:
        form = AuthenticationForm()
        return render(request, "accountapp/login.html", {"login_form": form})