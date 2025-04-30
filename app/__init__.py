from flask import Flask
from .config import Config
from .extensions import mongo
from .routes.rag import rag_bp
from dotenv import load_dotenv

def create_app():
    load_dotenv()
    app = Flask(__name__)
    app.config.from_object(Config)
    mongo.init_app(app,uri=app.config["MONGO_URI"])
    app.register_blueprint(rag_bp,url_prefix='/api')
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
    




# from flask_pymongo import PyMongo
# from dotenv import load_dotenv

# load_dotenv()

# mongo = PyMongo()
# ==========
# def create_app():
#     load_dotenv()
#     app = Flask(__name__)
#     app.config.from_object(Config)

#     mongo.init_app(app)
#     app.register_blueprint(rag_bp,url_prefix='/api')
#     return app
# ==========
# is this correct?