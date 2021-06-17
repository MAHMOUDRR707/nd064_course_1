from flask import Flask
import json
import logging
app = Flask(__name__)

##status
@app.route("/status")
def status():
    status = app.response_class(
        response = json.dumps({"result":"OK - healthy"}),
        status = 200,
        mimetype="application/json"
    )

    app.logger.info("health is ok ")
    return status

##metrics
@app.route("/metrics")
def metrics():
    metrics = app.response_class(
        response =json.dumps ({"status":"successful","code":0,"data":{"UserCount":140,"UserCountActive":23}}),
        status = 200,
        mimetype="application/json"
    )

    app.logger.info("metrics is ok too")

    return metrics

##home
@app.route("/")
def hello():

    app.logger.info("Home page is ok ")

    return "Hello World!"

if __name__ == '__main__':
    logging.basicConfig(filename='app.log',level=logging.DEBUG)
    app.run(threaded=True)



