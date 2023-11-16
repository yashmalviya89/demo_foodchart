from django.shortcuts import render, HttpResponseRedirect, redirect
from .urls import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages  # for django messaging service
from django.contrib.auth.decorators import (
    login_required,
)  # jis bhi route ko required bnana ho ki login hone pr hi dikhe vo page to isliye

# for encripted password check , login for mantaining the session
from django.contrib.auth import authenticate, login, logout  # predefined methods hai


def home(request):
    data = [
        {"name": "Yash Malviya", "address": "Indore", "age": 23},
        {"name": "Kapil Malviya", "address": "Delhi", "age": 27},
    ]
    return render(
        request, "index.html", context={"mydata": data}
    )  # yha pr hum context ka use krke ek key bna rhe he mydata name se jis se hum html me hmare variable ko access krenge


def services(request):
    # if request.method == "POST":
    #     check = request.POST["dishName"]
    #     print(check)
    return render(request, "services.html")


def contacts(request):
    return render(request, "contacts.html")


def order_food(request):
    return render(request, "order-food.html")


def login_page(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=username, password=password)
        if user:
            login(
                request, user
            )  # yha pr vo login kr dega or session me value dal denge login ke throgh
            return redirect("services")
        else:
            # Handle invalid login
            messages.error(request, "Invalid Username or Password")
            return redirect("login_page")

    return render(request, "login.html")


def register_page(request):
    if request.method == "POST":
        # Extract form data
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        username = request.POST["username"]
        password = request.POST["password"]

        # Check if the username is already taken
        print("Yash Msg")
        try:
            exists = User.objects.filter(username=username).exists()
        except Exception as e:
            print(f"Error checking if user exists: {e}")
        print(User.objects.filter(username=username))
        if User.objects.filter(username=username).exists():
            print("User exists")
            # Handle username already exists error
            messages.error(request, "Username already exists.")
            return redirect("/register/")  # Redirect to the register page

        # Create a new user
        print("data coming")
        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            # password=password # hum yha password field ko set nh krenge bcz password ko incripted bnana hai to ek method me dalna hoga yha vo normal string me save ho jaiga
        )
        user.set_password(password)  # Encrypt the password
        user.save()
        messages.success(request, "Account created successfully!")

        # Log the user in and redirect to a different page
        login(request, user)
        return redirect("services")

    return render(request, "register.html")


def logout_page(request):
    logout(request)  # ye session se lekr aajaiga
    return redirect("/login/")
