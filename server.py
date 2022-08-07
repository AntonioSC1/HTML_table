from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/template')
def template():
    student_info = [
        {'first_name': 'Micheal', 'last_name': 'Choi', 'full_name': 'Micheal Choi'},
        {'first_name': 'John', 'last_name': 'Supsupin', 'full_name': 'John Supsupin'},
        {'first_name': 'Mark', 'last_name': 'Guillen', 'full_name': 'Mark Guillen'},
        {'first_name': 'KB', 'last_name': 'Tonel', 'full_name': 'KB Tonel'}
    ]
    return render_template("index.html", student_info=student_info)


if __name__ == "__main__":
    app.run(debug=True)
