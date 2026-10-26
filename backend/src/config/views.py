
from django import forms
from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.utils.translation import gettext_lazy as _
from django.views.decorators.http import require_POST

from pets.models import Pet

User = get_user_model()


class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(
        label=_("Password"),
        min_length=8,
        widget=forms.PasswordInput,
    )

    password2 = forms.CharField(
        label=_("Confirm password"),
        widget=forms.PasswordInput,
    )

    class Meta:
        model = User
        fields = ("username", "email")
        labels = {
            "username": _("Username"),
            "email": _("Email"),
        }

    def clean(self):
        cleaned = super().clean()
        password1 = cleaned.get("password1")
        password2 = cleaned.get("password2")

        if password1 and password2 and password1 != password2:
            self.add_error(
                "password2",
                _("The passwords do not match."),
            )

        return cleaned

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])

        if commit:
            user.save()

        return user


class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = (
            "name",
            "species",
            "breed",
            "birth_date",
            "photo_url",
            "notes",
        )

        labels = {
            "name": _("Pet name"),
            "species": _("Species"),
            "breed": _("Breed"),
            "birth_date": _("Birth date"),
            "photo_url": _("Photo URL"),
            "notes": _("Notes"),
        }

        widgets = {
            "birth_date": forms.DateInput(
                attrs={"type": "date"}
            ),
            "notes": forms.Textarea(
                attrs={"rows": 3}
            ),
        }


def home(request):
    pets = (
        request.user.pets.all()
        if request.user.is_authenticated
        else []
    )

    return render(
        request,
        "home.html",
        {"pets": pets},
    )


def register_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard")

    form = RegisterForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.save()
        login(request, user)
        return redirect("dashboard")

    return render(
        request,
        "register.html",
        {"form": form},
    )


def login_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard")

    form = AuthenticationForm(
        request,
        data=request.POST or None,
    )

    if request.method == "POST" and form.is_valid():
        login(request, form.get_user())
        return redirect("dashboard")

    return render(
        request,
        "login.html",
        {"form": form},
    )


@login_required
def dashboard(request):
    if request.method == "POST":
        form = PetForm(request.POST)

        if form.is_valid():
            pet = form.save(commit=False)
            pet.owner = request.user
            pet.save()
            return redirect("dashboard")
    else:
        form = PetForm()

    pets = Pet.objects.filter(owner=request.user)

    return render(
        request,
        "dashboard.html",
        {
            "pets": pets,
            "form": form,
        },
    )


@login_required
@require_POST
def logout_view(request):
    logout(request)
    return redirect("home")
