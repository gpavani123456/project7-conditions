from django.shortcuts import render

# Create your views here.
def conditions(request):
    d={'a':50}
    return render(request,'wish.html',context=d)


def statements(request):
    d={'a':100,'b':200}
    return render(request,'statements.html',context=d)