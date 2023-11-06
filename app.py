from flask import Flask, request, render_template_string
from markupsafe import escape

app = Flask(__name__)



# flask --debug run

# https://docs.python.org/3/reference/datamodel.html#user-defined-functions

# {{self.__init__.__globals__.__builtins__.open("text.txt").read()}}
@app.route("/")
def home():
    name = "World"


    if request.args.get("name"):
        name = request.args.get("name")

    template = """
    <!DOCTYPE html>
    <html>
        <body>
            <p>Hello """ + name + """!</p>
            <p>Shopping List:</p>

            <ul>
                {% for item in ["Bread", "Apples", "Peaches", "Sugar", "Beans"] -%}
                    <li>{{item}}</li>
                {% endfor %}
            </ul>
        </body>
    </html>
    """

    return render_template_string(template)