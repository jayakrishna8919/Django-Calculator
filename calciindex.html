from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def main(request):
    context={}
    return render(request,'calciindex.html',context)

def calculate(request):
    if request.method=='POST':
        number_one = request.POST.get("number_one")
        number_two = request.POST.get("number_two")
        operation = request.POST.get("operation")
    if operation == 'add':
        result = float(number_one)+float(number_two)
        context = {'result':result}
        return render(request,'calciindex.html',context)
    elif operation == 'sub':
        result = float(number_one)-float(number_two)
        context = {'result':result}
        return render(request,'calciindex.html',context)
    elif operation == 'mul':
        result = float(number_one)*float(number_two)
        context = {'result':result}
        return render(request,'calciindex.html',context)
    elif operation == 'div':
        try:
            result = float(number_one)/float(number_two)
            context = {'result':result}
            return render(request,'calciindex.html',context)
        except ZeroDivisionError as error:
            return render(request,'calciindex.html',{'result':error})
    else:
        return render(request,'calciindex.html')
