from django.shortcuts import render, redirect
from .models import Newsletter
from django.contrib import messages


# Create your views here.
def newsletter(request):
    if request.method == "POST":
        email = request.POST["email"]

        if not email == "":
            newsletter = Newsletter(email=email)
            newsletter.save()
            messages.success(request, "Abonnement bien effectuer, merci.")
            return redirect('index')
        else:
            messages.error(request, "Une erreur s'est produite, merci de d'essayer plus tard.")
            return redirect('index')