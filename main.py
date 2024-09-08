from flask import Flask, request, make_response, redirect, render_template

app = Flask(__name__)
items =["arroz", "huevos", "cafe", "leche"]

@app.errorhandler(404)
def not_found_endpoint(error):
    return render_template('404.html', error=error)



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
app.run(host='0.0.0.0', port=81, debug=True) # debug=True es para debuguear el codigo 