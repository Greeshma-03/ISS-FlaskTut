from flask import Flask,render_template

app=Flask(__name__)


@app.route("/")
def mainfunc()->str:
    return "<h1>This is the page with main function</h1>"

@app.route("/about")
def aboutfunc()->str:
    return render_template("use.html",myname="random")

if __name__=="__main__":
    app.run(debug=True)

