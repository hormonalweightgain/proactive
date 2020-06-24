from django.shortcuts import render
from main.models import Patient
from main.forms import PatientForm 
from django.shortcuts import redirect


# Create your views here.
def homepage(request):
    form = PatientForm()
    if request.method == 'POST':
        form =PatientForm(request.POST)
        if form.is_valid():
            form.save()
            print('valid')
            return redirect('/homepage')
        else:
            print('invalid')

    context={
        "form":form,
    }

    return render(request,'main/homepage.html',context)


def test(request):
    context={}
    return render(request,'main/test.html',context)