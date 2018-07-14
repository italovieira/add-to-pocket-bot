from bot import app
from flask import request
from api.telegram import send_message

@app.route('/', methods=['POST'])
def hello():
    message = request.get_json().get('message')
    chat_id = message['chat']['id']
    send_message(chat_id, 'Hello there!')
    return 'OK'

if __name__ == '__main__':
    app.run()
