from django.http import HttpResponse

def URLtest(request):
    return HttpResponse("<h1>Test successfull</h1>")