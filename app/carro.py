class Carro:
    def __init__(self, request):
        self.request = request
        self.session = request.session 
        carro=self.session.get("carro")
        if not carro:
            carro=self.session["carro"]={}
        self.carro=carro

    def agregar(self, producto):
        if(str(producto.id) not in self.carro.keys()):
            self.carro[producto.id]={
                "producto_id" : producto.id,
                "nombre" : producto.nombre,
                "precio" : producto.precio,
                "precio_unitario" : producto.precio,
                "descuento" : producto.descuento,
                "cantidad" : 1,
                "imagen" : producto.imagen.url,
                "total" : producto.precio if not producto.descuento else round(producto.precio-(producto.precio*(producto.descuento / 100)))
            }
        else:
            for key, value in self.carro.items():
                if key==str(producto.id):
                    value["cantidad"]=value["cantidad"]+1
                    value["precio"]=value["precio"]+producto.precio
                    value["total"]=value["total"]+producto.precio if not producto.descuento else round(value["total"]+producto.precio-(producto.precio*(producto.descuento / 100)))
                    break
        self.guardar_carro()
    
    def guardar_carro(self):
        self.session["carro"]=self.carro
        self.session.modified=True

    def eliminar(self, producto):
        producto.id=str(producto.id)
        if producto.id in self.carro:
            del self.carro[producto.id]
            self.guardar_carro()

    def restar(self, producto):
        for key, value in self.carro.items():
            if key==str(producto.id):
                value["cantidad"]=value["cantidad"]-1
                value["precio"]=value["precio"]-producto.precio
                value["total"]=value["total"]-producto.precio if not producto.descuento else round(value["total"]-(producto.precio-(producto.precio*(producto.descuento / 100))))
                if value["cantidad"]<1:
                    self.eliminar(producto)
                break
        self.guardar_carro()

    def limpiar_carro(self):
        self.session["carro"]={}
        self.session.modified=True
