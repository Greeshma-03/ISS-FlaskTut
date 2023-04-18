from flask import Flask

app=Flask(__name__)

@app.route("/")

def hello()->str:

    def temp():
        return "hello"

    def temp2():
        return "heyy"

    final=temp()+temp2()

    return final

@app.route("/about")
def function2()->str:
    return "<h1>This is about page</h1>"


@app.route("/url1")    
@app.route("/url2")
def commonfunction()->str:
    return "<h2>example of a common function</h2>"


if __name__=="__main__":
    app.run(debug=True)