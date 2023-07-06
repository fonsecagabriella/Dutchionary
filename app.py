from flask import Flask, render_template, request, jsonify
from project import return_webcall, check_sentence


app = Flask (__name__)

# turn my file into a web application
@app.route("/")
def index():
    # return "hello, world"
    # name = request.args.get("name", "world") #this function can get a default value,  in this case, world
    return render_template("index.html")

# get input from user and generate dictionary definition in JSON format
@app.route("/get_input", methods=["POST"])
def get_input():
    w = request.form.get("word") # get word for user input
    # PS: for Get requests you use request.args.get("word")
    response = return_webcall(w)
    #print(response)
    if not response == False and not response == "Error":
        return render_template("definition.html", response = response)
    else:
        return render_template("error.html")
    ## Add return error page

@app.route("/get_sentence", methods=["POST"])
def get_sentence():
    zin = request.form.get("sentence")
    s = check_sentence(zin)
    #print(s)
    #html
    return jsonify({'html_code': '<p>'+ s+ '</p>' })


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
