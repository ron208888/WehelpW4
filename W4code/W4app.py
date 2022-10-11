from flask import Flask
from flask import request
from flask import redirect
from flask import render_template
from flask import session


app=Flask(
    __name__,
    
)
app.secret_key="test"

@app.route("/")
def index():
    return render_template("W4.html")

@app.route("/signin",methods=["POST"])
def signin():
    name=request.form["name"]
    keyword=request.form["keyword"]
    session["username"]=name
    session["userkeyword"]=keyword
    if name == "test" and keyword == "test":
        session.permanent=True
        return redirect("http://127.0.0.1:3000/member")
    elif name == "" or keyword == "":
        return redirect("http://127.0.0.1:3000/error?message=empty")
    else:
        return redirect("http://127.0.0.1:3000/error?message=inputerror")


@app.route("/member")
def member():
    name=session["username"]
    if session.permanent==False:
        return redirect("http://127.0.0.1:3000/")
    return render_template("member.html",name=name)

@app.route("/error")
def error():
    message=request.args.get("message")
    if message=="empty":
        return render_template("error.html",errortype="請輸入帳號、密碼")
    else:
        return render_template("error.html",errortype="帳號、或密碼輸入錯誤")

@app.route("/signout")
def signout():
    session.permanent=False
    return redirect("http://127.0.0.1:3000/")


app.run(port=3000)