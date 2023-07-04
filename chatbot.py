from flask import Flask, request, jsonify
import openai

openai.api_key = 'your-api-key'

app = Flask(__name__)

@app.route('/get_response', methods=['POST'])
def chatbot_response():
    user_text = request.json['message']

    response = openai.Completion.create(
      engine="text-davinci-002",
      prompt=user_text,
      max_tokens=150
    )

    bot_response = response.choices[0].text.strip()

    return jsonify({'message': bot_response})

if __name__ == '__main__':
    app.run(debug=True)
