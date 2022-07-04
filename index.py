import flask
import requests

# get request
JENKINS_AUTH_CODE = '<JENKINS_AUTH_CODE>'
app = flask.Flask(__name__) 
@app.route('/')
def index():
    return flask.render_template('From Bridge Server')
@app.get('/')
def main():
    # get JOB_ID, JOB_URL and RESPONSE from get request
    JOB_ID = flask.request.args.get('JOB_ID')
    JOB_URL = flask.request.args.get('JOB_URL')
    DECISION  = flask.request.args.get('RESPONSE')
# xhr.open("POST", "https://jenkins.neebal.com/job/Playpen/job/approval-button/25/input/Approval/abort");
# xhr.setRequestHeader("Authorization", "Basic c2h1YmhhbWdhaWt3YWQ6MTFlOTY5NzcwZWNjZWVlNWU5NWY0ZGE3Njk1Y2MzMGFjNw==");
    print(JOB_ID, JOB_URL, DECISION)

# RUn APP
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)