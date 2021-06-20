from flask import Flask, render_template, url_for, request
import requests

url = "https://besttime.app/api/v1/keys/pri_c1383a9ff6db4157b3606bca5ca95df7"

response = requests.request("GET", url)

app = Flask(__name__, static_folder="static")


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
    app.run()
