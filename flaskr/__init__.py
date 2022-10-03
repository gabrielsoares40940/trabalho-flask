import os
from flask import Flask
from flaskr import auth, blog


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.register_blueprint(auth.bp)
    app.register_blueprint(blog.bp)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )
    from flaskr import db
    db.init_app(app)

    return app
    #
    # if test_config is None:
    #     app.config.from_pyfile('config.py', silent=True)
    # else:
    #     app.config.from_mapping(test_config)
    #
    # try:
    #     os.makedirs(app.instance_path)
    # except OSError:
    #     pass
    #
    # @app.route('/hello')
    # def hello():
    #     return 'Hello world'
    #
    # return app


app = create_app()

app.run()
