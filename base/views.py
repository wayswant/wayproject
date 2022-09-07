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

                in_h = (sy.integrate(H11(r), (r, 0, np.infty)))
                y = sy.integrate((sy.integrate(in_h * (sy.sin(t)), (t, 0, np.pi))), (p, 0, 2 * np.pi))
                z = y * 27.2114

            elif element == "2":

                r, t, p = sy.symbols('x, theta, pi')

                def X1(r):
                    R1 = 2 * (n1 ** (3 / 2)) * np.e ** (-n1 * r)
                    return R1 * Y

                '''X(electron 1,2,3...)'''

                def X2(r):
                    R2 = 2 * (n2 ** (3 / 2)) * np.e ** (-n2 * r)

                    return R2 * Y

                r, t, p = sy.symbols('x, theta, pi')

                def in_s(a, b):
                    sab = (sy.integrate(a * b * (r ** 2), (r, 0, np.infty)))
                    return sy.integrate((sy.integrate(sab * (sy.sin(t)), (t, 0, np.pi))), (p, 0, 2 * np.pi))

                S11 = S22 = in_s(X1(r), X1(r))
                S12 = S21 = in_s(X1(r), X2(r))

                def H11(r):
                    dif1 = sy.diff(X1(r), r)
                    dif2 = sy.diff((r ** 2) * dif1, r)
                    return (X1(r)) * (((-0.5) * dif2) - ((n1 / r) * (X1(r)) * (r ** 2)) + (
                            ((n1 - 2) / r) * (X1(r)) * (r ** 2)))

                def H22(r):
                    dif1 = sy.diff(X2(r), r)
                    dif2 = sy.diff((r ** 2) * dif1, r)
                    return (X2(r)) * (((-0.5) * dif2) - ((n1 / r) * (X2(r)) * (r ** 2)) + (
                            ((n1 - 2) / r) * (X2(r)) * (r ** 2)))

                def H12(r):
                    dif1 = sy.diff(X2(r), r)
                    dif2 = sy.diff((r ** 2) * dif1, r)
                    return (X1(r)) * (((-0.5) * dif2) - ((n2 / r) * (X2(r)) * (r ** 2)) + (
                            ((n2 - 2) / r) * (X2(r)) * (r ** 2)))

                def in_h(a):
                    ha = (sy.integrate(a, (r, 0, np.infty)))
                    return sy.integrate((sy.integrate(ha * (sy.sin(t)), (t, 0, np.pi))), (p, 0, 2 * np.pi))

                H11 = in_h(H11(r))
                H22 = in_h(H22(r))
                H12 = H21 = in_h(H12(r))

                l = 0
                expansionr12 = 4 * np.pi / ((2 * l) + 1)
                kk = 2 * Y

                def in_x(a, b, c, d):
                    f = a + b
                    g = c + d
                    inC = kk ** 4 * (1 / f ** 3) * (
                            2 / g ** 2 - (1 / (f + g) ** 4) * (12 * f ** 2 + 8 * f * g + 2 * g ** 2)) * (
                                  a * b * c * d) ** (3 / 2)
                    inD = kk ** 4 * (1 / f ** 2) * (1 / (f + g) ** 4) * (8 * f + 2 * g) * (a * b * c * d) ** (3 / 2)
                    return (sy.integrate((sy.integrate((inC + inD) * (sy.sin(t)), (t, 0, np.pi))),
                                         (p, 0, 2 * np.pi))) * expansionr12

                V1111 = in_x(n1, n1, n1, n1)
                V2222 = in_x(n2, n2, n2, n2)
                V1122 = V2211 = in_x(n1, n1, n2, n2)
                V1212 = V2112 = V1221 = V2121 = in_x(n1, n2, n1, n2)
                V1112 = V1121 = V1211 = V2111 = in_x(n1, n1, n1, n2)
                V1222 = V2212 = V2122 = V2221 = in_x(n1, n2, n2, n2)

                k = 2
                C21 = (1 + (k ** 2) + (2 * k * S12)) ** (-0.5)
                C11 = C21 * k
                dn = 0.152

                EHF = ""

                while dn > 0.001:
                    '''A = old C21, then dn = A - C21(new)'''
                    A = C21

                    P11 = 2 * C11 * C11
                    P12 = 2 * C11 * C21
                    P21 = P12
                    P22 = 2 * C21 * C21

                    F11 = H11 + (0.5 * P11 * V1111) + (P12 * V1112) + (P22 * (V1122 - (0.5 * V1221)))
                    F12 = H12 + (0.5 * P11 * V1211) + (P12 * (((3 / 2) * V1212) - ((1 / 2) * V1122))) + (
                            0.5 * P22 * V1222)
                    F21 = F12
                    F22 = H22 + (P11 * (V2211 - (0.5 * V2112))) + (P12 * V2212) + (0.5 * P22 * V2222)

                    '''solve quadratic for E'''

                    Qa = (S11 * S22) - (S12 * S21)
                    Qb = -((F22 * S11) + (F11 * S22)) + ((F12 * S21) + (F21 * S12))
                    Qc = F11 * F22 - F12 * F21

                    '''determinant'''
                    D = (Qb ** 2) - (4 * Qa * Qc)
                    E1 = ((-Qb) + D ** 0.5) / (2 * Qa)
                    E2 = ((-Qb) - D ** 0.5) / (2 * Qa)

                    print("E1 and E2")
                    print(E1, E2)

                    k = -(F22 - (E2 * S22)) / (F21 - (E2 * S21))

                    C21 = (1 + (k ** 2) + (2 * k * S12)) ** (-0.5)
                    C11 = C21 * k

                    dn = A - C21

                    print("C21 and C11")
                    print(C21, C11)

                    EHF = E2 + (0.5 * ((P11 * H11) + (2 * P12 * H12) + (P22 * H22))) + 0

                '''1 hartree = 27.2114 eV
                experiment = -79.00
                EHF = -77.8700346963995
                EHF = -77.8700346963995
                Z1 = 1.45
                Z2 = 2.91
                '''
                E = EHF * 27.2114
                z = E

            elif element == "3":
                z = n1 * n2 * n3
            elif element == "4":
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
