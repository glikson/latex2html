import json
import boto3

def latex2html(latex):
    lambda_client = boto3.client('lambda')
    try: 
        FUNCTION_NAME = "diderot-test-latex2html"
        resp = lambda_client.invoke(FunctionName=FUNCTION_NAME, Payload=json.dumps({"latex":latex}), LogType="Tail")
        res = resp['Payload'].read().decode()
        html = json.loads(res)["html"]
        print html
    except botocore.exceptions.ClientError as e:
        print 'Lambda invocation exception: ' + str(e)
        html = "Error: " + str(e)
    return html

with open('example.tex') as f:
    latex = f.read()
print latex
html = latex2html(latex)
print html

