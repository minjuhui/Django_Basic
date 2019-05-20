from django.shortcuts import render

#main page
def index(request):
    return render(request,'index.html')