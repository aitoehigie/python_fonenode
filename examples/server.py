from flask import Flask
from flask import request
import fonenode
app = Flask(__name__)

@app.route("/", methods=["POST"])
def smsToCall():
    pass
    


if __name__ == "__main__":
    app.run(debug=True)


