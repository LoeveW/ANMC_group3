from flask import Flask, escape, request, render_template
from werkzeug.datastructures import ImmutableMultiDict

app = Flask(__name__)
PORT = 8080

sliders = {
    "slider1": 50,
    "slider2": 50,
    "slider3": 50,
    "slider4": 50,
    "slider5": 50,
    "slider6": 50,
    "slider7": 50,
    "slider8": 50,
    "slider9": 50,
    "slider10": 50
}

# Handler = http.server.SimpleHTTPRequestHandler


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        req = request.form;
        reqDict = req.to_dict(flat=False)
        print(reqDict)

    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True, port=8080, host='0.0.0.0')
