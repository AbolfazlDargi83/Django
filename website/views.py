from django.shortcuts import render

from django.http import HttpResponse,JsonResponse

def http_test(request):
    return HttpResponse("<h1>Hello World</h1>")


def json_test(request):
    return JsonResponse({'name':'Ali', 'age':20})

def index_view(request):
    return render(request,'index.html')

def contact_view(request):
    return render(request,'contact.html')

def about_view(request):
    return render(request,'about.html')

def web(request):
    return render(request, 'panel/index.html')