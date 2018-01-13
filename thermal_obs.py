import json

from flask import Flask
from flask import render_template
from flask import request

app=Flask(__name__)

@app.route("/api/v1.0/<component>/<method>", methods=['GET', 'POST'])
def get_component_status(component,method):
    if component=="motor":
        response=get_motor_status(method)
        return response
    else:
        return "component not monitored"
def get_motor_status(method):
    if method=="thermal":
        #read the thermal data
        data = request.get_json(silent=True)
        #compute the difference between armature and ambient temperature
        delta= data["thermaldata"]["ta"]-data["thermaldata"]["tm"]
        #computes the status of motor according to standard
        print (delta)
        #shows status
        return str(delta)
    else:
        return "method not monitored"
if __name__ == '__main__':
    app.run(port=5000, debug=True)
