import os
from flask import Flask, request, render_template, redirect, url_for
from flask_restful import Api
from dotenv import load_dotenv
from db import db
from controllers.info_controller import InfoController
from controllers.index_controller import IndexController
from controllers.heladeria_controller import HeladeriaController
from controllers.productos_controller import ProductosController
from controllers.ingredientes_controller import IngredientesController
from controllers.productos_ingredientes_controller import ProductosIngredientesController

load_dotenv()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = (f'mysql'
                                         f'://{os.getenv("USER_DB")}'
                                         f':{os.getenv("PASSWORD_DB")}'
                                         f'@{os.getenv("HOST_DB")}'
                                         f':{os.getenv("HOST_PORT")}'
                                         f'/{os.getenv("SCHEMA_DB")}')
db.init_app(app)
api = Api(app)


@app.route("/")
def main():
    return "Bienvenidos..."


@app.route("/heladeria", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("index.html")
    else:
        id_producto = request.form['idProducto']
        print("id:", id_producto)
    return render_template("heladeria.html")


api.add_resource(InfoController, '/info')
api.add_resource(IndexController, '/index')
#api.add_resource(HeladeriaController, '/heladeria')
api.add_resource(ProductosController, '/productos')
api.add_resource(IngredientesController, '/ingredientes')
api.add_resource(ProductosIngredientesController, '/productos_ingredientes')
