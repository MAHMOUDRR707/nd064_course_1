from flask import Flask
import json
app = Flask(__name__)

##status
@app.route("/status")
def status():
    status = app.response_class(
        response = json.dumps({"result":"OK - healthy"}),
        status = 200,
        mimetype="application/json"
    )
    return status

##metrics
@app.route("/metrics")
def metrics():
    metrics = app.response_class(
        response =json.dumps ({"status":"successful","code":0,"data":{"UserCount":140,"UserCountActive":23}}),
        status = 200,
        mimetype="application/json"
    )
    return metrics

##home
@app.route("/")
def hello():
    return "Hello World!"

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True)





