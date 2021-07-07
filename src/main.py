from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
import requests

url = "https://besttime.app/api/v1/keys/pri_c1383a9ff6db4157b3606bca5ca95df7"

response = requests.request("GET", url)

app = Flask(__name__, static_folder="static")

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/todos", methods=['POST', 'GET'])
def todos():
    # return render_template('todos.html', title='Todos')
    todo_list = Todo.query.all()
    return render_template("base.html", todo_list=todo_list)

# **************START ROUTINES FOR todo LIST***************
@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title")
    new_todo = Todo(title=title, complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("todos"))

@app.route("/update/<int:todo_id>")
def update(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for("todos"))

@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("todos"))

# **************END ROUTINES FOR todo LIST***************

@app.route("/map")
def mapview():
    return render_template('map.html', title='Map')

@app.route('/mapclick')
def mapclick():
    print('map clicked')
    address = request.args.get('address')
    name = request.args.get('name')
    print(address)
    print(name)
    url = "https://besttime.app/api/v1/forecasts"
    f = open("src/bestimekey.txt", "r")
    params = {
        'api_key_private': "pri_c1383a9ff6db4157b3606bca5ca95df7",
        'venue_name': name,
        'venue_address': address
    }
    response = requests.request("POST", url, params=params)
    print(response)
    return response.json()

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
