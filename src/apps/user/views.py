from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from apps.user.models import User
# Create your views here.


def login_page(request):

    if request.method == "POST":
        print(request.POST)
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is None:
            return render(request, 'login.html', context={"error": "username yoki parol xato"})
        login(request, user)
        return redirect("book_list_page")
    return render(request, 'login.html')


def register_page(request):
    data = {}
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = User.objects.filter(username=username)
        if user:
            data['error'] = "bu foydalanuvchi mavjud!"
        else:
            user = User.objects.create(
                first_name=full_name,
                username=username
            )
            user.set_password(password)
            user.save()
            login(request, user)
            return redirect('book_list_page')
    return render(request, 'register.html', context=data)


def logout_page(request):
    logout(request)
    return redirect("login_page")