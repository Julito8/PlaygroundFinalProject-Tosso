from django.http import HttpResponse


def saludo(request):
    return HttpResponse("Hola")

def tirar_dado(request):
    import random
    numero = random.randint(1, 6)
    if numero == 6:
        return HttpResponse(f"Has tirado el dado {numero}, Ganaste!")
    else:
        return HttpResponse(f"Tiraste el dado {numero}, sigue intentando")