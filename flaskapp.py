from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/correlation_matrix")
def correlation_matrix():
    return render_template("page2.html")

@app.route("/time_series")
def time_series():
    return render_template("page3.html")


if __name__ == '__main__':
    app.run()