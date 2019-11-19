from django.shortcuts import render
from .models import Employee
def showindex(request):
    return render(request,"index.html")


def adminindex(request):
    emp =Employee.objects.all()
    usr = request.POST.get("us")
    pas = request.POST.get("ps")
    ty = request.POST.get("se")
    q = Employee.objects.get(username=usr)
    if q.username and q.password!=pas:
        message="Please Enter correct Password"
    if (q.username==usr and q.password==pas) and q.type!=ty:
        message="Please Enter correct Password"
    if q.username==usr and q.password==pas and q.type==ty:
        message="welcome Admin"
    return render(request,"admin.html",{"msg":message})
