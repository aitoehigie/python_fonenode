from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def smsEndPoint():
   return request.data

if __name__ == "__main__":
    app.run(debug=True)


