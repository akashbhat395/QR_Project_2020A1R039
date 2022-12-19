from django.shortcuts import render
from qrcode import *

data=None

def home(request):
    global data
    if request.method == "POST":
  
            data = request.POST['data']
            img = make(data)
            img.save("static/image/test.png")

    else:
        print("Please enter data")
        
    return render(request,"home.html",{'data': data})

def about(request):
    return render(request,"about.html")   