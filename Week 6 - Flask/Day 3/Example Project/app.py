import flask
import database_manager # this is our module

app = flask.Flask(__name__)
database_manager.create_database()


@app.route("/")
@app.route("/products")
def products_page():
    data = database_manager.load_database()
    template_file = open('templates/my_template.html', 'r').read()
    css = open('style.css', 'r').read()

    return flask.render_template_string(template_file, products=data, additional_css=css)

app.run(debug=True)





