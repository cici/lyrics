from flask import Flask
from lyrics.models import db
from lyrics.controllers.song import main_blueprint
#from lyrics.controllers.blog import blog_blueprint

def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)

    db.init_app(app)

    app.register_blueprint(main_blueprint)
    #app.register_blueprint(blog_blueprint)

    return app

if __name__ == "__main__":
    app.run(debug=True)
