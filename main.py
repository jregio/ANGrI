# Add the current directory to Python path to help with imports
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from flask import Flask, render_template, jsonify, request, url_for
from model.utils import chinese_to_pinyin, chinese_to_english
from pypinyin import pinyin, Style
import pickle
from model.n_gram_model import NgramModel

# Create a custom unpickler to handle module imports
class CustomUnpickler(pickle.Unpickler):
    def find_class(self, module, name):
        if module == "n_gram_model":
            module = "model.n_gram_model"
        return super().find_class(module, name)

app = Flask(__name__, static_folder='static', static_url_path='/static')

# Load models
models = {}
for n in [1, 2, 3, 4]:
    model_path = os.path.join(os.path.dirname(__file__), f'model/models/ngram_{n}.pkl')
    if os.path.exists(model_path):
        with open(model_path, 'rb') as f:
            models[n] = CustomUnpickler(f).load()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sample', methods=['POST'])
def sample():
    n = int(request.json.get('n', 1))
    if n not in models:
        return jsonify({'error': 'Model not found'}), 404
    
    # Sample from the model
    chars = models[n].sample_ngram()
    if not chars:
        return jsonify({'error': 'Failed to sample'}), 500
    
    # Convert to pinyin
    pinyin = chinese_to_pinyin(chars)
    
    # Get translation (if available)
    translation = chinese_to_english(chars)
    
    return jsonify({
        'characters': chars,
        'pinyin': pinyin,
        'translation': translation
    })

if __name__ == '__main__':
    app.run(debug=True)
