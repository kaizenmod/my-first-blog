"""books URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, re_path, path
from django.conf.urls import url
from my_books import views

urlpatterns = [
	
    path('admin/', admin.site.urls),

	path('books/',views.bookshome,name='bookshome'),

    path('create/',views.bookscreate,name='bookscreate'),  
    re_path(r'(?P<id>\d+)/$',views.booksdetail,name='booksdetail'),
    re_path(r'$',views.bookslist,name='bookslist'),
    path('update/',views.booksupdate,name='booksupdate'),
    path('delete/',views.booksdelete,name='booksdelete'),

    path('',views.post_home,name='post_home'),

]
