import numpy as np
import sympy as sy
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
    Y = (1 / (4 * np.pi)) ** (1 / 2)
    z = ''
    ee1 = ''
    try:
        if request.method == "POST":
            n1 = eval(request.POST.get('num1'))
            n2 = eval(request.POST.get('num2'))
            n3 = eval(request.POST.get('num3'))
            element = request.POST.get('element')
            if element == "1":

                r, t, p = sy.symbols('x, theta, pi')

                def X1(r):
                    R1 = 2 * (n1 ** (3 / 2)) * np.e ** (-n1 * r)
                    return R1 * Y

                def H11(r):
                    dif1 = sy.diff(X1(r), r)
                    dif2 = sy.diff((r ** 2) * dif1, r)
                    return (X1(r)) * ((-0.5) * dif2 - ((1 / r) * (X1(r)) * (r ** 2)))

                y = sy.integrate((sy.integrate((sy.integrate(H11(r), (r, 0, np.infty))) * (sy.sin(t)), (t, 0, np.pi))),(p, 0, 2 * np.pi))
                z = y*27.2114

            elif element == "1":

                r, t, p = sy.symbols('x, theta, pi')

                def X1(r):
                    R1 = 2 * (n1 ** (3 / 2)) * np.e ** (-n1 * r)
                    return R1 * Y

                def H11(r):
                    dif1 = sy.diff(X1(r), r)
                    dif2 = sy.diff((r ** 2) * dif1, r)
                    return (X1(r)) * ((-0.5) * dif2 - ((1 / r) * (X1(r)) * (r ** 2)))

                y = sy.integrate((sy.integrate((sy.integrate(H11(r), (r, 0, np.infty))) * (sy.sin(t)), (t, 0, np.pi))),
                                 (p, 0, 2 * np.pi))
                z = y * 27.2114

            elif element == "2":
                z = n1 * n2 * n3
            elif element == "3":
                z = n1 / n2 / n3

    except:
        z = "Invalid opr ...."

        '''Rnl, Rn(electron 1,2,3...)'''
        '''n = 1'''



    # def X1(r1):
    #     R11 = 2 * (z ** (3 / 2)) * np.e ** (-z * r1)
    #     return R11 * Y
    #
    # r, t, p = sy.symbols('x, theta, pi')
    # r1, r2 = sy.symbols('x, x')
    #
    # ee1 = sy.integrate((X1(r1) * (X1(r1) * (r1 ** 2))), (r1, 0, r2))
    # ee = (sy.integrate((sy.integrate(ee1 * (sy.sin(t)), (t, 0, np.pi))), (p, 0, 2 * np.pi)))

    return render(request, 'energy.html', {'z': z, 'ee1': ee1, })

# planck = 6.63
#
#
# def niceweb1_1(request):
#     context = {"planck": planck,}
#     return render(request, 'niceweb1.1.html', context)


def index(request):
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

    return render(request, 'index.html', {'z': z, 'a': a})
