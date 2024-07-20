from flask import render_template, make_response, request
from flask_restful import Resource
from models.heladeria import Heladeria


class HeladeriaController(Resource):

    def get(self):
        heladeria = Heladeria("La Heladeria")
        items = heladeria.lista_productos()
        return make_response(render_template("index.html", items=items))

    def post(self):
        id_producto = request.form['idProducto']
        print("id:", id_producto)
        return make_response(render_template("heladeria.html"))
