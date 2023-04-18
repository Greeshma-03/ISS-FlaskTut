from flask import Flask, render_template, request, jsonify

app = Flask(__name__, static_folder='static')

@app.route("/")
def func():
    return "<h1>Main page function</h1>"

@app.route("/usespython")    
def usepython():
    fruits = ["apple", "banana", "mango"]
    return render_template("use4.html", sendvar=fruits, myfruit="appl")

@app.route('/results', methods=['POST', 'GET'])
def handle_post_request():
    if request.method == 'POST':
        return "posted data"
    else:
        return "No data submitted."

if __name__ == "__main__":
    app.run(debug=True)
