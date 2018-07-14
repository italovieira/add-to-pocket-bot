from bot import app
import requests

def api_request(method, parameters=None):
    if parameters is None:
        parameters = {}

    URL = app.config['API_URL'] + method
    r = requests.get(URL, params=parameters)
    return r.json()

def get_updates():
    return api_request('getUpdates')['result']

def get_last_update():
    return get_updates()[-1]

def get_last_message():
    return get_last_update()['message']

def send_message(chat_id, text):
    params = {'chat_id': chat_id, 'text': text}
    api_request('sendMessage', params)
