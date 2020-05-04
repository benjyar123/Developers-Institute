import flask
# imports the flask module

app = flask.Flask(__name__)
# instance of the class flask

# decorator that controls webpage route name
@app.route('/')
def index():
    return "Hello World!"

@app.route('/home')
def home():
    return "<h1 style='color:red;'>This is the home page!</h1>"



# localhost: 127.0.0.1

@app.route('/home/<username>')
def pyuser(username):
    template =  '''
<html>
    <head>
        <title>Home Page - Microblog</title>
    </head>
    <body>
        <h1>Hello, {{ name }}! How are you ? Is this working?</h1>
    </body>
</html>'''
    html = flask.render_template_string(template, name=username)
    return html


@app.route('/blog')
def bloglist():
    template =  '''
<html>
    <head>
        <title>Blog Page</title>
    </head>
    <body>
        <h1>Blog Posts</h1>
        <p>
            <ul>
                <li>{{ article1 }}</li>
                <li>{{ article2 }}</li>
                <li>{{ article3 }}</li>
    </body>
</html>'''

    article1 = "Favourite Ice Creams"
    article2 = "Fast Cars"
    article3 = "Cheeses of England"

    html = flask.render_template_string(template, article1=article1, article2=article2, article3=article3)
    return html


if __name__ == "__main__":
    app.run(debug=True,port=5000)