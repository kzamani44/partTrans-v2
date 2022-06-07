from django.shortcuts import render
from googletrans import Translator
from django.urls import reverse
from django.http import HttpResponseRedirect
from django import forms


class profileDetails(forms.Form):
    username = forms.CharField(label="Name")
    email = forms.CharField(label="Email")
# Create your views here.



def index(request):
    if request.method == "POST":
        name = profileDetails(request.POST)
        mail = profileDetails(request.POST)
        if name.is_valid() & mail.is_valid():
           username = name.cleaned_data["username"]
           usermail = mail.cleaned_data["email"]
           request.session["usermail"] = usermail
           request.session["user"] = username
           return HttpResponseRedirect(reverse("home"))

        else:
            return render(request, "register.html", {
                "name": name,
                "mail":mail
            })

    return render(request, "register.html", {
        "profile" : profileDetails()
    })           
      
def human(request):
    return render(request, "index.html", {
        "user": request.session["user"],
        "usermail": request.session["usermail"]
    })

def home(request):
    return render(request, "homepage.html")    