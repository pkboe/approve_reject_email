import flask
import requests

# get request
JENKINS_AUTH_CODE = '<JENKINS_AUTH_CODE>'
app = flask.Flask(__name__) 
@app.get('/')
def index(): 
    return flask.render_template_string(''' hello ''')
@app.route("/approve", methods=["GET"])
def main():
    # get JOB_ID, JOB_URL and RESPONSE from get request
    BUILD_ID = flask.request.args.get('BUILD_ID')
    JOB_URL = flask.request.args.get('JOB_URL')
    DECISION  = flask.request.args.get('DECISION')
# xhr.open("POST", "https://jenkins.neebal.com/job/Playpen/job/approval-button/25/input/Approval/abort");
# xhr.setRequestHeader("Authorization", "Basic c2h1YmhhbWdhaWt3YWQ6MTFlOTY5NzcwZWNjZWVlNWU5NWY0ZGE3Njk1Y2MzMGFjNw==");
    print(BUILD_ID, JOB_URL, DECISION)
    # send request to jenkins
    res = flask.make_response('OK',200)
    res.headers['Content-Type'] = 'text/plain'
    res.headers.add('Access-Control-Allow-Origin',
                    dict(flask.request.headers).get("Origin"))
    return res


# RUn APP
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)