import os
from flask import Flask
from flask_restful import Api
from dotenv import load_dotenv
from db import db
from controllers.info_controller import InfoController

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


api.add_resource(InfoController, '/info')
