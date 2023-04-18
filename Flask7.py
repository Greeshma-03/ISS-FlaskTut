from flask import Flask, render_template, request, jsonify

app = Flask(__name__, static_folder='static')

@app.route("/")
def func():
    return "<h1>Main page function</h1>"

@app.route("/usespython")    
def usepython():
    fruits = ["apple", "banana", "mango"]
    return render_template("use4.html", sendvar=fruits, myfruit="appl")


@app.route('/data', methods=['GET','POST'])
def get_data():
    if request.method=='POST':
        
        return "posted your data"

    else:    
        data = {'name': 'John', 'age': 30, 'city': 'New York'}
        return data


if __name__ == "__main__":
    app.run(debug=True)
