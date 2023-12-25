from flask import Flask

from mainapp.views import views

app = Flask(__name__)


app.register_blueprint(views, url_prefix='')