from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "Test"

@app.route('/test')
def test():
    return render_template("app.html")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
