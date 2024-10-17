from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from routes import EpisodeResource, GuestResource, AppearanceResource
from flask_restful import Api
from app import db


# Initialize the app and db
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    migrate.init_app(app, db)
    api = Api(app)

    # Registering Resources
    api.add_resource(EpisodeResource, '/episodes', '/episodes/<int:id>')
    api.add_resource(GuestResource, '/guests')
    api.add_resource(AppearanceResource, '/appearances')
     
    return app

if __name__ == '__main__':
    app= create_app()
    app.run(debug=True)
