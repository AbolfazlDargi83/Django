from django.urls import path
from website.views import http_test,json_test, index_view, contact_view, about_view , web

urlpatterns = [
    path('http_test', http_test),
    path('json_test',json_test),
    path("", index_view),
    path("contact",contact_view),
    path("about",about_view),
    path('panel', web)
]