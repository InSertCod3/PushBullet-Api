import requests
import json

class API (object):
    def __init__ (self, apikey):
        self.apikey = apikey

    def push_message (self, title = None, msg = None):
        endpoint = "https://api.pushbullet.com/v2/pushes"
        headers = {'Access-Token': str(self.apikey),
                    'content-type': 'application/json'
                    }

        data = '''{"body":"%s",
                "title":"%s",
                "type":"note"}''' % (msg, title)

        REQ = requests.post(endpoint, data=str(data), headers=headers)
        return json.loads(REQ.text)
'''
a = API(API_KEY_HERE)
a.push_message('Message','Hey how is it going')
'''
