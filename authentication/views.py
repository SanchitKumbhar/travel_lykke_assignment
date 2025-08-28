from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request,"home.html")

def render_authentication(request):
    return render(request,"authentication.html")

def process_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email=request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)  

        if user is not None:
            loggedin = login(request,user)
            return render(request,"travel_options.html")
        else:
            return HttpResponse(
                "<h1> Not Registered User!<br>Either username is wrong or password</h1>"
            )
        
def process_signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email=request.POST.get("email")
        password = request.POST.get("password")

        if username or email or password is not None:
            user=User(username,email,password)
            login(user)
            return render(request,"travel_options.html")

def process_logout(request):
    logout(request)
    return redirect("/")