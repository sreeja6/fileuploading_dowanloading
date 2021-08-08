from django.shortcuts import render,redirect
from app.models import Filedetails

def fileupload(request):
    return render(request,"fileupload.html",{"data": Filedetails.objects.all()})
def save_file(request):
    na = request.POST.get("f1")
    file = request.FILES['f2']
    Filedetails(Name=na,file=file).save()
    return redirect('main')
