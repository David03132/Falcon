import requests
import json
from transbank.error.transbank_error import TransbankError
from transbank.webpay.webpay_plus.transaction import Transaction
from django.shortcuts import redirect, render
from django.http.response import HttpResponse


class Carro:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        self.url_transbank= ""
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
                "cantidad" : 1,
                "imagen" : producto.imagen.url
            }
        else:
           for key, value in self.carro.items():
               if key==str(producto.id):
                   value["cantidad"]=value["cantidad"]+1
                   value["precio"]=value["precio"]+producto.precio
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
                if value["cantidad"]<1:
                    self.eliminar(producto)
                break
        self.guardar_carro()

    def limpiar_carro(self):
        self.session["carro"]={}
        self.session.modified=True
        
    """def compra_transbank():
        print("Webpay Plus Transaction.create")
        buy_order = str('ordenCompra12345678')
        session_id = str('sesion1234557545')
        amount = 1000
        return_url = 'http://www.comercio.cl/webpay/retorno'

        create_request = {
            "buy_order": buy_order,
            "session_id": session_id,
            "amount": amount,
            "return_url": return_url,
        }

        response = (Transaction()).create(buy_order, session_id, amount, return_url)

        print(response)
        print(create_request)
        return render('webpay/plus/create.html', request=create_request, response=response)"""