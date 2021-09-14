from flask import Flask, request, render_template
from flask.views import MethodView
from markupsafe import escape

import random
import json

app = Flask(__name__)

class Index(MethodView):
    def get(self,a,b):
        return json.dumps( {"RANDOM":random.randint(a,b)} )
    def post(self):
        return "hello from post"


# app.add_url_rule('/',view_func=Index.as_view("Home"))
app.add_url_rule('/<int:a>/<int:b>',view_func=Index.as_view("Home"))

if __name__ == '__main__':
    app.run(debug=True,port=5001)