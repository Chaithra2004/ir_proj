from flask import Flask, render_template, request, jsonify
from news_ir import NewsIRSystem

app = Flask(__name__)
ir_system = NewsIRSystem()

# Load and index documents at startup
data_dir = 'Data'
ir_system.load_json_files(data_dir)
ir_system.build_index()
print(f"Indexed {len(ir_system.documents)} documents.")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search')
def search():
    query = request.args.get('q', '')
    if not query:
        return jsonify([])
    
    results = ir_system.search(query)
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
