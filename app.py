from flask import Flask, request, render_template
app = Flask(__name__)
# decorator calls age() when / is called
@app.route('/',methods=["GET","POST"])
def age():
    age = None
    if request.method == "POST":
        age = request.form["age"]
    return render_template("index.html",age=age)
if __name__ == "__main__":
    app.run(debug=True)