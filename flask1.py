from flask import Flask

app= Flask(__name__)  #__name__ helps the app to know the route path

@app.route("/")
def index ():
    return "hello world"

@app.route('/home/<username>')
def home(username):
    return"<h4>hello %s<h4>" %username

if __name__ == "__main__":
    app.run(debug=True)




