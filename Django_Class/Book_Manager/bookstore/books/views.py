from django.shortcuts import render, redirect
from books.models import booksModel

def home(request):
    return render(request, 'home.html')

def bookList(request):
    books = booksModel.objects.all()

    return render(request, 'book_list.html',{'books':books})

def bookForm(request):
    
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        category = request.POST.get('category')
        publish_date = request.POST.get('publishDate')
        description = request.POST.get('description')

        bookAdd = booksModel.objects.create(
            BookTitle = title,
            BookAuthor = author,
            BookCategory = category,
            BookPublishDate = publish_date,
            BookDescription = description
        )
        bookAdd.save()
        return redirect('bookList')
    return render(request, 'book_form.html',)

def bookUpdate(request, id):
    books= booksModel.objects.get(id=id)
    if request.method == 'POST':
        id = id,
        title = request.POST.get('title')
        author = request.POST.get('author')
        category = request.POST.get('category')
        publish_date = request.POST.get('publishDate')
        description = request.POST.get('description')

        bookAdd = booksModel.objects.create(
            BookTitle = title,
            BookAuthor = author,
            BookCategory = category,
            BookPublishDate = publish_date,
            BookDescription = description
        )
        bookAdd.save()
        return redirect('bookList')
    return render(request, 'book_update.html', {'books': books})

def bookDelete(request, id):
     book = booksModel.objects.get(id=id)
     book.delete()
     return redirect('bookList')

    
