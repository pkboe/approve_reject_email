import json
import flask
import requests

# get request
PASSWORD = '114c1639ef95c33ef3e253fa8392c3a889'
app = flask.Flask(__name__) 

def trigger(JOB_URL, BUILD_ID, PROCEED): #Yes or No
    if PROCEED == 'Yes':
        url = JOB_URL+'/'+BUILD_ID+'/wfapi/inputSubmit?inputId=Approval&proceed='+PROCEED
    else:
        url = JOB_URL+'/'+BUILD_ID+'/input/Approval/abort'
    # post request with form data and auth
    # Add Form Data To POST Request
    # multipart form data
    headers = {'Content-Type': 'multipart/form-data',}
    form_data = {'json': json.dumps({"parameter": []})}
    res = requests.post(url, auth=('pranilkharche', PASSWORD), data=form_data)
    # add form data to request
    return res



@app.get('/')
def index(): 
    return flask.render_template_string(''' hello ''')
@app.route("/trigger", methods=["GET"])
def main():
    # get JOB_ID, JOB_URL and RESPONSE from get request
    BUILD_ID = flask.request.args.get('BUILD_ID')
    JOB_URL = flask.request.args.get('JOB_URL')
    PROCEED  = flask.request.args.get('PROCEED')
# xhr.open("POST", "https://jenkins.neebal.com/job/Playpen/job/approval-button/25/input/Approval/abort");
# xhr.setRequestHeader("Authorization", "Basic c2h1YmhhbWdhaWt3YWQ6MTFlOTY5NzcwZWNjZWVlNWU5NWY0ZGE3Njk1Y2MzMGFjNw==");
    print(BUILD_ID, JOB_URL, PROCEED)
    # send request to jenkins

    res_from_trigger = trigger(JOB_URL, BUILD_ID, PROCEED)
    if (res_from_trigger.status_code == 200 or res_from_trigger.status_code == 201):
        
        res = flask.make_response(flask.jsonify({"Pipeline URL": JOB_URL,
        "Proceed": PROCEED  }), 200)
    else:
        res = flask.make_response(flask.render_template_string('''
        <h1>Something went wrong</h1>
        '''+str((res_from_trigger.content))), 500)
        # print everything from response


    res.headers.add('Access-Control-Allow-Origin',
                    dict(flask.request.headers).get("Origin"))    
    return res


# RUn APP
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)