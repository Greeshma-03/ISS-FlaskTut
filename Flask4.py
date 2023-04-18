from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def func():
    return "<h1>Main page function</h1>"

@app.route("/usespython")    
def usepython():
    fruits=["apple","banana","mango"]
    return render_template("use2.html",sendvar=fruits,myfruit="apple")


if __name__=="__main__":
    app.run(debug=True)