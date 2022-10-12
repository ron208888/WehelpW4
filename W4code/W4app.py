from email import message
from flask import Flask
from flask import request
from flask import redirect
from flask import url_for
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
    session["userkey"]=keyword
    if name == "test" and keyword == "test":
        session.permanent=True
        return redirect("http://127.0.0.1:3000/member")
    elif name == "" or keyword == "":
        message="請輸入帳號、密碼"
        return redirect(url_for("error",message=message))
    else:
        message="帳號、或密碼輸入錯誤"
        return redirect(url_for("error",message=message))


@app.route("/member")
def member():
    name=session["username"]
    if session.permanent==False:
        return redirect("http://127.0.0.1:3000/")
    return render_template("member.html",name=name)

@app.route("/error")
def error():
    message=request.args.get("message")
    return render_template("error.html",errortype=message)
    
@app.route("/signout")
def signout():
    session.permanent=False
    return redirect("http://127.0.0.1:3000/")


@app.route("/requestnum")
def requestnum():
    requestNum=request.args.get("requestNum")
    return redirect (url_for("square",requestNum=requestNum))

@app.route("/square/<string:requestNum>")
def square(requestNum):
    
    requestNum=int(requestNum)
    result=0
    result=requestNum**2

    return render_template("square.html",result=result)

app.run(port=3000)