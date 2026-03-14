from django.shortcuts import render, redirect
from .models import Book


# Create your views here.


def book_list_page(request):
    print(request.user)
    if not request.user.is_authenticated:
        return redirect("login_page")
    
    books = Book.objects.all()
    context = {
        "books": books
    }
    return render(request, 'book-list.html', context=context)


def book_create_page(request):

    if request.method == "POST":
        print(request.POST)
        book_name = request.POST.get("book_name")
        book_status = request.POST.get("book_status", None)
        author = request.user
        Book.objects.create(
            title=book_name,
            is_active=True if book_status is not None else False,
            author=author
        )
        return redirect("book_list_page")

    return render(request, 'book-create.html')


def book_delete_page(request, pk):
    book = Book.objects.filter(id=pk)
    if book.exists():
        if book.first().author == request.user:
            book.first().delete()
    return redirect("book_list_page")

