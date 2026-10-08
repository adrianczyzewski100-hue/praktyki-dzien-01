from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    imie = None
    wiadomosc = None
    if request.method == "POST":
        imie = request.form.get("imie")
        wiadomosc = request.form.get("wiadomosc")
    return render_template("index.html", imie=imie, wiadomosc=wiadomosc)

if __name__ == "__main__":
    app.run(debug=True)