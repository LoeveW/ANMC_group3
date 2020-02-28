from flask import Flask, escape, request, render_template

app = Flask(__name__)
PORT = 8080


# Handler = http.server.SimpleHTTPRequestHandler


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        req = request.
        print(req)
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True, port=8080, host='0.0.0.0')
