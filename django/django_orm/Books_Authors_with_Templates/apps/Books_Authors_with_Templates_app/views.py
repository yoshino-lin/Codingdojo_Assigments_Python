from django.shortcuts import render, HttpResponse, redirect
from apps.Books_Authors_with_Templates_app.models import *

def index(request):
    context={
        "books_list":Book.objects.all(),
    }
    return render(request,'Books_Authors_with_Templates_app/index.html',context)

def authors(request):
    context={
        "authors_list":Author.objects.all(),
    }
    return render(request,'Books_Authors_with_Templates_app/authors.html',context)

def book_add(request):
    the_book_title = request.POST.get('title_add')
    the_book_description = request.POST.get('description_add')
    Book.objects.create(title=the_book_title,desc=the_book_description)
    return redirect('/')

def author_add(request):
    the_author_first_name = request.POST.get('first_name_add')
    the_author_last_name = request.POST.get('last_name_add')
    the_author_note = request.POST.get('notes_add')
    Author.objects.create(first_name = the_author_first_name, last_name = the_author_last_name, notes = the_author_note)
    return redirect('/authors')

def add_author_to_book(request,book_id):
    this_book = Book.objects.get(id=book_id)
    this_author_id = request.POST.get("author_id")
    this_author = Author.objects.get(id=this_author_id)
    this_book.author.add(this_author)
    return redirect('/')

def add_book_to_author(request,author_id):
    this_author = Author.objects.get(id=author_id)
    this_book_id = request.POST.get("book_id")
    this_book = Book.objects.get(id=this_book_id)
    this_book.author.add(this_author)
    return redirect('/authors')

def display_book(request,book_id):
    this_book = Book.objects.get(id=book_id)
    this_book_authors = this_book.author.all()
    context = {
        "this_book" : this_book,
        "this_book_authors" : this_book_authors,
        "authors_list":Author.objects.all(),
    }
    return render(request,'Books_Authors_with_Templates_app/books.html',context)

def display_author(request,author_id):
    this_author = Author.objects.get(id=author_id)
    this_author_books = this_author.books.all()
    context = {
        "this_author" : this_author,
        "this_author_books" : this_author_books,
        "books_list":Book.objects.all(),
    }
    return render(request,'Books_Authors_with_Templates_app/author.html',context)

def destroy_session(request):
    return redirect('/')
