from flask import Flask, request, make_response, redirect, render_template

app = Flask(__name__)
items =["ITEM1", "ITEM2", "ITEM3", "ITEM4"]

@app.route("/index")
def index():
    user_ip_information = request.remote_addr
    response = make_response(redirect("/show_information_address"))
    response.set_cookie("user_ip_information", user_ip_information)
    return response
    #return f"Hola tu IP es: {user_ip_information}"

@app.route("/show_information_address")
def show_information():
    user_ip = request.cookies.get("user_ip_information")
    #return f"Hola tu IP es: {user_ip}"
    context = {
        "user_ip":user_ip,
        "items":items
    }
    #return render_template("/ip_information.html", user_ip=user_ip, )
    return render_template("/ip_information.html", **context )
app.run(host='0.0.0.0', port=81, debug=False) # debug=True es para debuguear el codigo 