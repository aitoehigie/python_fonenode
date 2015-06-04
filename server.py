from flask import Flask
from flask import request
import fonenode
app = Flask(__name__)

@app.route("/", methods=["GET"])
def smsToCall():
    fonenode.quick_call(to=request.args.get("from"), text="Dont let go",\
    from_who="2348029401212")


if __name__ == "__main__":
    app.run(debug=True)


