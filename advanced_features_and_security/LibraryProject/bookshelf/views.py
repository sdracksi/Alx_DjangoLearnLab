from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required, login_required
from .models import Book
from django.db.models import Q
from .forms import BookForm


# Create your views here.
@login_required
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
        query = request.GET.get("q", "")
        if query:
            books = Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))
        else:
            books = Book.objects.all()
        return render(request, "bookshelf/book_list.html", {"books": books})
   

@login_required
@permission_required('bookshelf.can_create', raise_exception=True)
def book_create(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm()
    return render(request, "bookshelf/book_form.html", {"form": form})

@login_required
@permission_required('bookshelf.can_delete', raise_exception=True)
def book_delete(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return redirect("book_list")

@permission_required('bookshelf.can_edit', raise_exception=True)
def book_edit(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.publication_year = request.POST.get('publication_year')
        book.save()
        return redirect('book_list')
    return render(request, 'bookshelf/book_form.html', {'book': book})

