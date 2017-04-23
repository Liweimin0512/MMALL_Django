from django.shortcuts import render
from django.contrib.auth import authenticate, login
# Create your views here.


def userlogin(request):
    if request.method == "POST":
        user_name = request.POST.get("username", "")
        pass_word = request.POST.get("password", "")
        user = authenticate(username=user_name,password=pass_word)
        if user is not None:
            login(request, user)
            return render(request, "index.html")
        else:
            return render(request, "signIn.html", {})

    elif request.method == "GET":
        return render(request, "signIn.html", {})