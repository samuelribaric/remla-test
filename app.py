from flask import Flask, request
from flasgger import Swagger

app = Flask(__name__)

swagger = Swagger(app)

@app.route('/', methods = ["POST"])

def predict():
    msg = request.get_json().get("msg")
    return{
        "result": "Message was: " + msg,
    }

app.run(host = "0.0.0.0", port=8080, debug=True)