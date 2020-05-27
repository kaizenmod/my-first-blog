# Create your views here.

from django.shortcuts import render

from django.http import HttpResponse
from .models import My_books
from django.shortcuts import get_object_or_404

#def post_home(request):
 #   response = "<h1>Здесь расположены прочитанные мной книги и книги, которые я собираюсь прочесть</h1>"
  #  return HttpResponse(response)

def post_home(request):
	return render(request, "index.html", {})

def bookshome(request):
	content={
		"title":"Домашняя страница книг"
		}
	return render(request,"index.html",content)

def bookscreate(request):
	content={
		"title":"Создание книги"
		}
	return render(request,"index.html",content)

def booksdetail(request,id=1):
	#instance=My_books.objects.get(id=1)
	instance=get_object_or_404(My_books,id=id)
	content={
		"title":instance.title,
		"instance":instance,
		}
	return render(request,"booksdetail.html",content)

def bookslist(request):
	querybook=My_books.objects.all
	content={
		"title":"Библиотека книг гражданина Иванова А.А.",
		"object_list":querybook,
		}
	return render(request, "index.html", content)

def booksupdate(request):
	content={
		"title":"Редактирование книги"
		}
	return render(request, "index.html", content)

def booksdelete(request):
	content={
		"title":"Удаление книги"
		}
	return render(request, "index.html", content)


