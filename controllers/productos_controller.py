from flask import render_template, make_response
from flask_restful import Resource
from models.productos import Productos


class ProductosController(Resource):

    def get(self):
        items = Productos.query.all()
        for item in items:
            if item.vaso is None:
                item.vaso = ""
            if item.volumen is None:
                item.volumen = "0"
        return make_response(render_template("productos.html", items=items))
