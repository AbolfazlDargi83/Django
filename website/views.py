from django.shortcuts import render

from django.http import HttpResponse,JsonResponse

def http_test(request):
    return HttpResponse("<h1>Hello World</h1>")


def json_test(request):
    return JsonResponse({'name':'Ali', 'age':20})

def index_view(request):
    return HttpResponse("<h1>This is index page</h1>")

def contact_view(request):
    return HttpResponse("<h1>This is contact page</h1>")

def about_view(request):
    return HttpResponse("<h1>This is about page</h1>")
