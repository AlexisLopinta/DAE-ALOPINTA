from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'titulo': "calculadora",
    }
    return render(request, 'calculadora/calculadora.html', context)

def calcular(request):
    if request.method == 'POST':
        num1 = request.POST.get('num1')
        num2 = request.POST.get('num2')
        operacion = request.POST.get('operacion')
        resultado = 0
        if operacion == 'suma':
            resultado = int(num1) + int(num2)
        elif operacion == 'resta':
            resultado = int(num1) - int(num2)
        elif operacion == 'multiplicacion':
            resultado = int(num1) * int(num2)
        mensaje_resultado = f"La {operacion} de {num1} + {num2} = {resultado}."
        return render(request, 'calculadora/resultado.html', {'mensaje_resultado': mensaje_resultado})
    else:
        return render(request, 'calculadora/calculadora.html')


