from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import *
from django.contrib.auth.decorators import (
    login_required,
)  # jis bhi route ko required bnana ho ki login hone pr hi dikhe vo page to isliye


# Create your views here.


@login_required(login_url="/login/")
def add_dishes(request):
    if request.method == "POST":
        data = request.POST
        dishName = data.get("dishName")
        dishDesc = data.get("dishDesc")
        dishPrice = data.get("dishPrice")
        dishImage = request.FILES.get("dishImage")

        print(dishName)
        print(dishDesc)

        Dish.objects.create(
            dishName=dishName,
            dishDesc=dishDesc,
            dishPrice=dishPrice,
            dishImage=dishImage,
        )

        return redirect("/show-dishes/")

    return render(request, "add-dishes.html")


# page ko direct dekhne pr nh dikhega vo login page pr chla jaiga
@login_required(login_url="/login/")
def show_dishes(request):
    dishes = Dish.objects.all()
    print("Data is coming")
    return render(request, "show-dishes.html", {"dishes": dishes})


@login_required(login_url="/login/")
def order_food(request):
    dishes = Dish.objects.all()
    return render(request, "order-food.html", {"dishes": dishes})


@login_required(login_url="/login/")
def delete_dish(request, id):
    print("here is the ", id)
    # dish = get_object_or_404(Dish, pk=dish_id)
    # dish.delete()

    # or

    dish = Dish.objects.get(id=id)
    dish.delete()
    # return redirect("order-food.html")
    return redirect("order-food.html")


def update_dish(request):
    pass
