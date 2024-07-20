import common.funciones as funciones
from models.productos import Productos
from models.ingredientes import Ingredientes

"""
Clase que contiene los atributos y funciones propias de la Heladeria.
"""


class Heladeria:
    def __init__(self, nombre: str):
        self.__nombre = nombre
        self.__lista_productos = self.lista_productos()
        self.__venta_del_dia = 0

    def get_nombre(self) -> str:
        return self.__nombre

    def get_venta_del_dia(self) -> float:
        return self.__venta_del_dia

    def producto_mas_rentable(self) -> str:
        return funciones.producto_mas_rentable(self.__lista_productos)

    def vender(self, nombre_producto: str) -> bool:
        resultado = False
        producto_vender = None
        for producto in self.__lista_productos:
            if producto.nombre == nombre_producto:
                producto_vender = producto
        if producto_vender is not None:
            lista_ingredientes = producto_vender.ingredientes
            ingredientes_completos = True
            for ingrediente in lista_ingredientes:
                "Validamos para cada ingrediente el inventario"
                if ingrediente.sabor is not None and ingrediente.inventario < 1:
                    ingredientes_completos = False
                    break
                if ingrediente.sabor is None and ingrediente.inventario < 0.2:
                    ingredientes_completos = False
                    break
            if ingredientes_completos:
                "Como los ingredientes cumplen el inventario, entonces descontamos."
                for ingrediente in lista_ingredientes:
                    "Descontamos del inventario"
                    if ingrediente.sabor is not None and ingrediente.inventario >= 1:
                        ingrediente.inventario = (ingrediente.inventario - 1)
                    if ingrediente.sabor is None and ingrediente.inventario >= 0.2:
                        ingrediente.inventario = (ingrediente.inventario - 0.2)
                self.__venta_del_dia = self.__venta_del_dia + producto_vender.precio
                resultado = True
        return resultado

    def lista_productos(self):
        productos = Productos.query.all()
        for item in productos:
            if item.vaso is None:
                item.vaso = ""
            if item.volumen is None:
                item.volumen = "0"
        return productos

    def lista_ingredientes(self):
        ingredientes = Ingredientes.query.all()
        for item in ingredientes:
            if item.vegetariano:
                item.vegetariano = "Si"
            else:
                item.vegetariano = "No"
            if item.sabor is None:
                item.sabor = ""
        return ingredientes
