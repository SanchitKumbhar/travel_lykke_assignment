from django.shortcuts import render,HttpResponse,redirect
from django.http import JsonResponse
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
import json
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
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
            user=User.objects.create_user(username=username,email=email,password=password)
            login(request,user)
            return render(request,"travel_options.html")

def process_logout(request):
    logout(request)
    return redirect("/")


@login_required
def update_profile(request):
        if request.method == "POST":
            data = json.loads(request.body)
            user = request.user
            response = {}

            username = data.get("username")
            email = data.get("email")
            password = data.get("password")

            if username:
                user.username = username
            if email:
                user.email = email
            if password:
                user.set_password(password)
                update_session_auth_hash(request, user)  # Keep user logged in after password change

            user.save()
            response["status"] = "success"
            return JsonResponse(response)
        else:
            return JsonResponse({"error": "Invalid request method"}, status=400)
        

def render_profile(request):
    return render(request,"profile.html")