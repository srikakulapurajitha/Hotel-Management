from django.shortcuts import render
from employee.models import employeedetails


'''this function used to insert employee forms field to db by using django ORM'''
def employeeform(request):
    if request.method=='GET':
        return render(request,'employeeform.html')
    else:
       employeedetails(
            EMPLOYEE_NAME=request.POST.get('EMPLOYEE_NAME'),
            DATE_OF_JOINING=request.POST.get('DATE_OF_JOINING'),
            SALARY=request.POST.get('SALARY'),
            MOBILE=request.POST.get('MOBILENUMBER'),
            DESIGNATION=request.POST.get('DESIGNATION'),
            GENDER=request.POST.get('GENDER')
        ).save()
       return render(request,'employeeform.html')
    
'''this function used to display emp deatils'''
def empdetails(request):
    empdat=employeedetails.objects.all().values()
    return render(request,'empdetails.html',{'empdat':empdat})