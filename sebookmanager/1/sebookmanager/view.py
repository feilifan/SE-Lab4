from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from books.models import Book,Author
import datetime
def search(request):
    my_list=[]
    lists=[]
    otherBooks=[]
    if 's' in request.GET:
        s = request.GET['s']
        authors=Author.objects.filter(Name=s)
        for author in authors:
            my_list.append(author)
            books=Book.objects.filter(AuthorId=author)
            my_list.append(books)
            lists.append(my_list)
            my_list=[]
        otherBooks = Book.objects.filter(Title__icontains=s) 
        return render_to_response('book_list.html',
            {'lists': lists,'otherBooks':otherBooks, 's': s})
    return render_to_response('book_list.html',)

def home(request):
    return render_to_response('home.html',{'test':'hello'})
def add_book(request):
    errors=[]
    if request.GET:
        if request.GET['update']=='1':
            update=True
        else:
            update=False
        dic={'update':update,'errors':errors,'ISBN':request.GET['ISBN'],'AuthorId':request.GET['AuthorId'],'Title':request.GET['Title'],'Publisher':request.GET['Publisher'],'PublishDate':request.GET['PublishDate'],'Price':request.GET['Price'],}
        my_Book=Book.objects.filter(ISBN=request.GET['ISBN'])
        my_Author=Author.objects.filter(AuthorId=request.GET['AuthorId'])
        if my_Book:
            if update:
                errors.append(False)
            else:    
                errors.append(True)
        else:
            errors.append(False)
        if my_Author: 
            errors.append(False)
        else:
             errors.append(True)
        if(errors[0] or errors[1]):
            return render_to_response('input.html',dic)
        else:
            get=request.GET
            if update:
                my_Book[0].AuthorId=my_Author[0]
                my_Book[0].Publisher=get['Publisher']
                my_Book[0].PublishDate=get['PublishDate']
                my_Book[0].Price=get['Price']
                my_Book[0].save()
            else:  
                new_book=Book(ISBN=get['ISBN'],Title=get['Title'],AuthorId=my_Author[0],Publisher=get['Publisher'],PublishDate=get['PublishDate'],Price=get['Price'])
                new_book.save()
            return HttpResponseRedirect('/add_success/')
    return render_to_response('input.html')
def add_success(request):
    return render_to_response('add_success.html')
def update(request):
    if request.GET:
        my_book=Book.objects.filter(ISBN=request.GET['ISBN'])
        date=my_book[0].PublishDate
        dic={'update':True,'ISBN':my_book[0].ISBN,'Title':my_book[0].Title,'AuthorId':my_book[0].AuthorId,'Publisher':my_book[0].Publisher,'PublishDate':date.strftime('%Y-%m-%d'),'Price':my_book[0].Price,}
        return render_to_response('input.html',dic)
    return HttpResponseRedirect('/')
def delete(request):
    if request.GET:
        my_book=Book.objects.filter(ISBN=request.GET['ISBN'])
        my_book[0].delete()
        return HttpResponseRedirect('/search_result/?s='+request.GET['s'])
    return HttpResponseRedirect('/')
def display(request):
    if request.GET:
        my_book=Book.objects.filter(ISBN=request.GET['ISBN'])
        date=my_book[0].PublishDate
        dic={'display':True,'ISBN':my_book[0].ISBN,'Title':my_book[0].Title,'AuthorId':my_book[0].AuthorId,'Publisher':my_book[0].Publisher,'PublishDate':date.strftime('%Y-%m-%d'),'Price':my_book[0].Price,'AuthorId':my_book[0].AuthorId.AuthorId,
             'Name':my_book[0].AuthorId.Name,'Age':my_book[0].AuthorId.Age,'Country':my_book[0].AuthorId.Country,}
        return render_to_response('input.html',dic)
    return HttpResponseRedirect('/')
def add_author(request):
    if request.GET:
        dic={'Name':request.GET['Name'],'Age':request.GET['Age'],'Country':request.GET['Country'],}
        my_Author=Author.objects.filter(AuthorId=request.GET['AuthorId'])
        if my_Author:
            dic['error']=True
            return render_to_response('add_author.html',dic)
        else:
            my_Author=Author(AuthorId=request.GET['AuthorId'],Name=request.GET['Name'],Age=request.GET['Age'],Country=request.GET['Country'],)
            my_Author.save()
            return HttpResponseRedirect('/add_success/')
    return render_to_response('add_author.html')
            