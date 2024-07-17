from db import db


class Ingredientes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(), nullable=False)
    precio = db.Column(db.Float(), nullable=False)
    calorias = db.Column(db.Integer(), nullable=False)
    vegetariano = db.Column(db.Bool(), nullable=False)
    inventario = db.Column(db.Float(), nullable=False)
    sabor = db.Column(db.String(), nullable=True)
