from db import db


class Productos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(), nullable=False)
    precio = db.Column(db.Float(), nullable=False)
    vaso = db.Column(db.String(), nullable=True)
    volumen = db.Column(db.Integer(), nullable=True)

    ingredientes = db.relationship('ProductosIngredientes', backref="ingredientes", lazy=True)
