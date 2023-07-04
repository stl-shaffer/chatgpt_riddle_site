from flask import Flask, request, jsonify
from ChatBotAPI import get_response # This is hypothetical

app = Flask(__name__)

@app.route('/get_response', methods=['POST'])
def chatbot_response():
    user_text = request.json['message']
    bot_response = get_response(user_text) # This is a hypothetical function, replace with actual function call to your API.
    return jsonify({'message': bot_response})

if __name__ == '__main__':
    app.run(debug=True)
