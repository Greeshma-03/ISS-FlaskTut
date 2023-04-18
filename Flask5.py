from flask import Flask, render_template

app=Flask(__name__,static_folder='static')

@app.route("/")
def func():
    return "<h1>Main page function</h1>"

@app.route("/usespython")    
def usepython():
    fruits=["apple","banana","mango"]
    return render_template("use3.html",sendvar=fruits,myfruit="appl")


if __name__=="__main__":
    app.run(debug=True)