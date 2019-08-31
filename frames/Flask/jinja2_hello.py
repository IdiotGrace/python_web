from flask import Flask, session
from datetime import datetime
from flask import request, render_template

app = Flask(__name__)


@app.route("/get_index")
def index():
    return render_template(
        "template.html",
        navigation=[
            'http://www.baidu.com', 'http://www.163.com', 'http://www.sina.com'
        ],
        a_variable="First Jinja2")


if __name__ == '__main__':
    app.run()