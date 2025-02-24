from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# def index(request):
#     return HttpResponse("Hello World!!!")

def index(request):
    my_dict={
        'insert_something':"views.pyのinsert_something部分です。",
        'name':'yasunari',
        'test_titles':["title 1","title 2","title 3"],
    }
    return render(request, 'httpserverapp/index.html',my_dict)