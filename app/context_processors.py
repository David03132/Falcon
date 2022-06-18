from .models import Categorias

def extras(request):
	lista_categorias = Categorias.objects.all().order_by('nombre')
	return {'categorias':lista_categorias}

def importe_total_carro(request):
	total=0
	if request:
		if "carro" in request.session:
			for key, value in request.session["carro"].items():
				total= total + int(value["precio"])
	return {"importe_total_carro":total}

def total_carro(request):
    total=0
    if request:
        if "carro" in request.session:
            for key, value in request.session["carro"].items():
                total= total + int(value["cantidad"])
    return {"total_carro":total}
