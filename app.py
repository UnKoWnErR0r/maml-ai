from flask import Flask, render_template, request, jsonify
import torch

app = Flask(__name__)

# Load your AI model here
# model = torch.load('path_to_your_model')  # Replace with your model loading code

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.json.get('message')
    
    # Run the input through your AI model and get the response
    # For now, we just echo the input as a placeholder
    ai_response = f"AI Response to: {user_input}"

    # In reality, you'd pass the `user_input` to your model and return its output
    return jsonify({"response": ai_response})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
