import flask

myapp = flask.Flask(__name__)

@myapp.route('/')
def index():
    return "Flask Lesson 2 site"

@myapp.route('/home')
def home(): # CONTROLLER
    #MODEL - might go and get username from database
    myname = "Benjy"
    fruits = ["apples", "oranges", "bananas"]
    # template_string = """
    # <h1>Hello</>
    # <p>This is a paragraph</p>
    # <p>My name is {{name}}.</>
    # """
    #
    # html = flask.render_template_string(template_string, name = myname)
    # or just render template if linking somewhere else in html file

    #VIEW
    html = flask.render_template("home.html", name=myname, fruits=fruits)

    return html

@myapp.route('/blog')
def blog():

    blog_1 = "Sandwiches"
    blog_2 = "The Queen"
    blog_3 = "Another sterotypically English thing"

    html = flask.render_template("blog.html", blog1=blog_1, blog2=blog_2, blog3=blog_3)

    return html

if __name__ == '__main__':
    myapp.run(debug=True)

