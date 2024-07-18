from db import db


class ProductosIngredientes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_productos = db.Column(db.Integer, db.ForeignKey("productos.id"), nullable=False)
    id_ingredientes = db.Column(db.Integer, db.ForeignKey("ingredientes.id"), nullable=False)

    producto = db.relationship('Productos', foreign_keys=[id_productos])
    ingrediente = db.relationship('Ingredientes', foreign_keys=[id_ingredientes])
