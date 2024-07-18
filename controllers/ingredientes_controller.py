
from flask import render_template, make_response
from flask_restful import Resource
from models.ingredientes import Ingredientes


class IngredientesController(Resource):

    def get(self):
        items = Ingredientes.query.all()
        for item in items:
            print("Vegetariano:", item.vegetariano)
            if item.vegetariano:
                item.vegetariano = "Si"
            else:
                item.vegetariano = "No"
            if item.sabor is None:
                item.sabor = ""
        return make_response(render_template("ingredientes.html", items=items))
