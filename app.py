from flask import Flask, render_template, request
from groq import Groq

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Task1.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the user input question
    question = request.form['question']  # Assuming 'question' is the name of the input field

    # Initialize the Groq client
    client = Groq(
        api_key='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',
    )

    # Make the chat completion request
    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": question}],
        model="llama-3.1-8b-instant",  # You can adjust the model as needed
    )

    # Extract the AI's response
    response = chat_completion.choices[0].message.content.replace('*','')

    # Return the response to the template
    return render_template('Task1.html', question=question, response=response)

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=8000)
