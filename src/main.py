from flask import Flask, render_template

app = Flask(__name__,static_folder="static")

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/todos")
def todos():
    return render_template('todos.html', title='Todos')

if __name__ == "__main__":
    app.run()
