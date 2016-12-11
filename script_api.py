import os
from botocore.awsrequest import AWSRequest
from botocore.auth import SigV4Auth
from botocore.endpoint import BotocoreHTTPSession
from botocore.endpoint import EndpointCreator
import botocore.endpoint
from botocore.credentials import Credentials


def execute_script():

    # APIリクエスト先のURL
    url = "https://script.api.cloud.nifty.com/2015-09-01"
    # APIリクエスト時のパラメータを設定
    params = {
        'ScriptIdentifier': 'test.js',
        'Method': 'GET',
        'Header': '{}',
        'Body': '{}',
        'Query': '{"name":"Umino"}',
    }
    # APIリクエストに必要なヘッダーの設定
    headers = {
        'X-Amz-Target': '2015-09-01.ExecuteScript',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    credentials = Credentials(os.environ["ACCESS_KEY_ID"], os.environ["SECRET_ACCESS_KEY"])
    request = AWSRequest(method="POST", url=url, data=params, headers=headers)
    SigV4Auth(credentials, "ExecuteScript", 'east-1').add_auth(request)
    response = BotocoreHTTPSession().send(request.prepare())
    return response

res = execute_script()
print(res)
print(res.text)
