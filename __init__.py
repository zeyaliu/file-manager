from flask import Flask
import controller
from flask.ext.bootstrap import Bootstrap


app = Flask(__name__, static_url_path='')
app.config['SECRET_KEY'] = 'mxcvjnjd';
bootstrap = Bootstrap(app)


app.add_url_rule('/', view_func=controller.index)
app.add_url_rule('/signup', methods=['POST'], view_func=controller.signup)
app.add_url_rule('/feedback', methods=['GET','POST'], view_func=controller.feedback)
app.add_url_rule('/uplfile', methods=['GET', 'POST'], view_func=controller.uplfile)
app.add_url_rule('/file', view_func=controller.file)



