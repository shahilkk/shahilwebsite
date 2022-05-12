from django.shortcuts import render,redirect
from .models import Details

# Create your views here.




def index(request):    
    return render(request,'index.html')  


def message(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        message=request.POST['message']
        print(name,email,message)
        details = Details(name=name,email=email,address=message)
        details.save()
        return redirect('shahil:index')