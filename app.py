from flask import Flask, request, render_template_string
from markupsafe import escape
import builtins
app = Flask(__name__)



# flask --debug run
# python3 app.py

# https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/07-Input_Validation_Testing/18-Testing_for_Server_Side_Template_Injection
# https://hackmd.io/@Chivato/HyWsJ31dI
# https://docs.python.org/3/reference/datamodel.html#user-defined-functions
# https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Server%20Side%20Template%20Injection#jinja2---basic-injection

# {{self.__init__.__globals__.__builtins__.open("text.txt").read()}}
# {{self.__init__.__globals__.__builtins__.open("/etc/passwd").read()}}
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
                    {%- for item in [
                        {"name": "Bread", "purchased": True},
                        {"name": "Bananas", "purchased": True},
                        {"name": "Apples", "purchased": True},
                        {"name": "Sugar", "purchased": False},
                        {"name": "Beans", "purchased": False},
                        {"name": "Carrots", "purchased": False}
                        ]  
                    -%}
                    
                        {% if item.purchased %}
                            <li><s>{{item.name}}</s></li>
                        {% else %}
                            <li>{{item.name}}</li>
                        {% endif %}
                        
                    {% endfor %}
            </ul>
        </body>
    </html>
    """

    return render_template_string(template)


@app.route("/fixed")
def home_fixed():
    name = "World"

    if request.args.get("name"):
        name = request.args.get("name")

    shopping_list = [
        {"name": "Bread", "purchased": True},
        {"name": "Bananas", "purchased": False},
        {"name": "Apples", "purchased": True},
        {"name": "Sugar", "purchased": False},
        {"name": "Beans", "purchased": False},
        {"name": "Carrots", "purchased": False}
    ]

    template = """
        <!DOCTYPE html>
        <html>
            <body>
                <p>Hello {{name}}!</p>
                <p>Shopping List:</p>
                
                <ul>
                    {%- for item in shopping_list  -%}
                    
                        {% if item.purchased %}
                            <li><s>{{item.name}}</s></li>
                        {% else %}
                            <li>{{item.name}}</li>
                        {% endif %}
                        
                    {% endfor %}
                </ul>
                
            </body>
        </html>
        """

    return render_template_string(template, name=name, shopping_list=shopping_list)


if __name__ == '__main__':
    app.run(host='0.0.0.0')


