from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def home(request):
    return render(request, 'home.html')


def room(request):
    return render(request, 'room.html')


def niceweb(request):
    return render(request, 'niceweb.html')


def niceweb2(request):
    a = 121212
    z = ''
    try:
        if request.method == "POST":
            n1 = eval(request.POST.get('num1'))
            n2 = eval(request.POST.get('num2'))
            n3 = eval(request.POST.get('num3'))
            z = n1 + n2 + n3
            opr = request.POST.get('opr')
            if opr == "+":
                z = n1 + n2 + n3
            elif opr == "-":
                z = n1 - n2 - n3
            elif opr == "*":
                z = n1 * n2 * n3
            elif opr == "/":
                z = n1 / n2 / n3

    except:
        z = "Invalid opr ...."

    return render(request, 'niceweb2.html', {'z': z, 'a': a})


def energy(request):
    a = 121212
    z = ''
    try:
        if request.method == "POST":
            n1 = eval(request.POST.get('num1'))
            n2 = eval(request.POST.get('num2'))
            n3 = eval(request.POST.get('num3'))
            z = n1 + n2 + n3
            opr = request.POST.get('opr')
            if opr == "+":
                z = n1 + n2 + n3
            elif opr == "-":
                z = n1 - n2 - n3
            elif opr == "*":
                z = n1 * n2 * n3
            elif opr == "/":
                z = n1 / n2 / n3

    except:
        z = "Invalid opr ...."

    return render(request, 'energy.html', {'z': z, 'a': a})

# planck = 6.63
#
#
# def niceweb1_1(request):
#     context = {"planck": planck,}
#     return render(request, 'niceweb1.1.html', context)
