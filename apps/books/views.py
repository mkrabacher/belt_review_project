# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..users.models import User
from ..books.models import *
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def books(request): 
    last_3 = Review.objects.all()
    last_3_in_ascending_order = last_3.order_by('-date_added')[:3]
    context = {
        'users':User.objects.all(),
        'curr_user':User.objects.get(id=request.session['curr_user_id']),
        'books':Book.objects.all(),
        'recent_reviews':last_3_in_ascending_order,
    }
    return render(request, 'books/index.html', context)

def bookPage(request, number):
    context = {
        'book':Book.objects.get(id=number)
    }
    return render(request, 'books/book.html', context)

def addBook(request):
    context = {
        'authors':Author.objects.all(),
        'authors_num':len(Author.objects.all())
    }
    return render(request, 'books/addBook.html', context)

def createBookReview(request):
    if request.method == "POST":
        title = request.POST['bookTitle']

        try:
            author = request.POST['authorList']
            if Author.objects.get(name=author):
                #add error message here
                return redirect('/books/add')
        except:
            if request.POST['authorNew'] == '':
                # add error message here    
                return redirect('/books/add')
            author = request.POST['authorNew']
            Author.objects.create(name=author)
    
        review = request.POST['review']
        rating = request.POST['rating']

        Book.objects.create(title=title, author=Author.objects.get(name=author))

        review = request.POST['review']
        rating = request.POST['rating']
        reviewer = User.objects.get(id=request.session['curr_user_id'])

        Review.objects.create(content=review, rating=rating, reviewer=reviewer, book=Book.objects.last())

    return redirect('/books')

def createReview(request):
    if request.method == "POST":

        book = Book.objects.get(id=request.POST['book_id'])
        review = request.POST['review']
        rating = request.POST['rating']
        reviewer = User.objects.get(id=request.session['curr_user_id'])

        review_curr = book.reviews.filter(reviewer__id=request.session['curr_user_id'])

        if len(review_curr) > 0:
            reviewObj = book.reviews.get(reviewer__id=request.session['curr_user_id'])
            reviewObj.content = review
            reviewObj.rating = rating
            reviewObj.save()
        else:
            Review.objects.create(content=review, rating=rating, reviewer=reviewer, book=Book.objects.last())

    return redirect('/books')

def delReview(request):
    if request.method == "POST":
        review = Review.objects.get(id=request.POST['rev_id'])
        review.delete()

    return redirect('/books/' + request.POST['book_id'])