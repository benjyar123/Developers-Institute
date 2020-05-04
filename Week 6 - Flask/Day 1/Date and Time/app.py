# ALSO NOT WORKING NO IDEA WHY


import flask
import datetime

app = flask.Flask(__name__)


x = datetime.datetime.now()
print(x)

@app.route('/time')
def date_and_time():
    template =  '''
<html>
    <head>
        <title>Home Page</title>
    </head>
    <body>
        <h1>The date and time right now is: {{ time }}!</h1>
    </body>
</html>'''
    html = flask.render_template_string(template, time=x)
    return html


if __name__ == "__main__":
    app.run(debug=True,port=5000)