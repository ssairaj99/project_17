from django.shortcuts import render

# Create your views here.

def mkdb(request):
    return render(request,'mkdb.html')