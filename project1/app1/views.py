from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
# Create your views here.

def display(request):
    return HttpResponse("hello world")

def display1(request,a):
    return HttpResponse(a)

def display2(request,c):
    return HttpResponse(c)

def reversename(request,b):
    rev = ""
    for i in b :
        rev = i + rev
    return HttpResponse(rev)

def abc(request):
    return render(request,'index.html')

def form(request):
    if request.method == "POST" :
        name=request.POST['name']
        age=request.POST['age']
        return render(request,'form.html',{'data': name, 'age':age})
    else:
        return render(request,'form.html')
    
def fars(request):
    if request.method == "POST" :
        name=request.POST['fname'] ##same as input name="fname" insife form in html
        age=request.POST['fage']  ##same as input name="fage" insife form in html
        return render(request,'formnew.html',{'A':name, 'B':age})
    else:
        return render(request,'form.html')
    
def fact(request):
    if request.method == "POST"  :
        number = int(request.POST['num'])
        f = 1
        for i in range(number) :
            if i >= 1 :
                
                f = f * i
        return render(request,'result.html',{'result':f})
    else:
        return render(request,'factorial.html') 

def naame(request):
    if request.method == "POST":
        name = request.POST['string']
        rev = ""
        for i in name:      
            rev = i + rev
        return render(request,'result.html',{'R':rev})
    else:
        return render(request,'reversestring.html')
    
def register(request):
    if request.method == "POST":
        Name = request.POST['name']
        Roll_num = request.POST['roll_num']
        Age = request.POST['age']
        Mark = request.POST['mark']

        student = Student.objects.create(name=Name,roll_number=Roll_num,age=Age,mark=Mark)
        student.save()
        return HttpResponse("completed")
    return render(request,'registeradmin.html')

def view_students(request):
    student = Student.objects.all()
    return render(request,'viewstudents.html',{'all_student':student})

def search_student(request):
    if request.method == "POST":
        search = request.POST['search']
        data = Student.objects.filter(name__icontains=search) ##name=search(full have to type the name)But icontains, 
        return render(request,'result.html',{'datas':data})   ##when type any letter the whole related to that letter will appear

    else:
        return render(request,'registeradmin.html')

def delete_student(request):
    if request.method == "POST":
        search = request.POST['search']
        data = Student.objects.get(roll_number=search)
        data.delete()
        return HttpResponse("deleted")
    else:
        return render(request,'registeradmin.html')

def update_student(request):
    if request.method == "POST":
        Roll_no = request.POST['roll_no']
        Name = request.POST['name']
        Age = request.POST['age']
        Mark = request.POST['mark']

        data = Student.objects.filter(roll_number=Roll_no).update(name=Name,age=Age,mark=Mark)
        student = Student.objects.get(roll_number=Roll_no)
        return render(request,'result.html',{'updated':student})
    else:
        return render(request,'registeradmin.html')
    
def temp1(request):
    return render(request,'temp1.html')
def temp2(request):
    return render(request,'temp2.html')
