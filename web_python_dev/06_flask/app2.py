from flask import Flask, url_for, redirect, render_template

app = Flask(__name__)


@app.route('/hello/<name>')
def hellomichael(name):
    print(url_for("static", filename="css2.css"))
    return f'Hello World! {name}'


@app.route("/login")
def login():
    return redirect(url_for("hellomichael", name="Michael"))

@app.route("/login1")
def login1():
    name = 'michael ming'
    age = 18
    msg = "一起加油！"
    return render_template("template1.html", name=name, age=age, msg=msg)

if __name__ == "__main__":
    app.run(debug=True, port=8080)