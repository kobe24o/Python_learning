from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World!'


@app.route("/user/<username>")
def show_user_name(username):
    return f"User name is {username}"


@app.route("/post/<int:post_id>")
def show_post_id(post_id):
    return f"Post id is {post_id}"

if __name__ == "__main__":
    app.run(debug=True, port=8080)
