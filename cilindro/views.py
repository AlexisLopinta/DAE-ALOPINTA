from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'titulo': "cilindro",
    }
    return render(request, 'cilindro/cilindro.html', context)

def respuesta(request):
    if request.method == 'POST':
        altura = float(request.POST.get('altura'))
        diametro = float(request.POST.get('diametro'))
        radio = diametro / 2
        volumen = round(3.14159 * radio**2 * altura, 2)
        return render(request, 'cilindro/cilindro.html', {'volumen': volumen})
    else:
        return render(request, 'cilindro/cilindro.html')
