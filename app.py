from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
@app.route("/mihail")
def hello():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
# top kek we are number one ALO YOBA SKOLKO MOZHNO
