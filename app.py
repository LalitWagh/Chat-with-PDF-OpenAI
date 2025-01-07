from flask import Flask, request, render_template, jsonify
from backend.process_pdf import extract_text_from_pdf, clean_text
from backend.query_handler import handle_query

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    text = extract_text_from_pdf(file)
    return jsonify({"extracted_text": clean_text(text)})

@app.route('/query', methods=['POST'])
def query():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON input"}), 400
    text = data.get('text', '')
    user_query = data.get('query', '')
    if not text or not user_query:
        return jsonify({"error": "Missing text or query parameter"}), 400
    response = handle_query(text, user_query)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
