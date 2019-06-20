import datetime, os

from src.models.chat import Chat
from src.models.trainChatBot import TrainChatBot
from src.utility import constant

__author__ = 'ravinathTudu'

from flask import Flask, render_template, request, jsonify

app = Flask(__name__,template_folder='src/templates',static_folder='src/static')

@app.route('/')
def home_template():
    return render_template('chatting.html')


@app.route('/chatting')
def login_template():
    return render_template('chatting.html')


@app.route('/chatting', methods=['POST'])
def client_user():
    chat = Chat()
    client_data = request.form['user']
    result = chat.train_data(client_data)
    return jsonify({'success': True,
                    'message': 'Successfully',
                    'data': result.serialize()})


if __name__ == '__main__':
    if constant.Constants.IS_TRAIN:
        t = TrainChatBot()
    app.run(port=8080, host='0.0.0.0', debug=False,)

