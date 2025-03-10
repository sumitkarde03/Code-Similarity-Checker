from flask import Flask, request, jsonify
from flask_cors import CORS
from algorithms.kmp import kmp_search
from algorithms.trie import Trie
from algorithms.rolling_hash import rolling_hash

app = Flask(__name__)
CORS(app)

@app.route('/compare', methods=['POST'])
def compare_code():
    data = request.json
    code1 = data.get("code1", "")
    code2 = data.get("code2", "")

    if not code1 or not code2:
        return jsonify({"error": "Both code snippets are required"}), 400

    trie = Trie()
    for line in code1.splitlines():
        trie.insert(line.strip())

    matches = sum(1 for line in code2.splitlines() if trie.search(line.strip()))
    total_lines = max(len(code1.splitlines()), len(code2.splitlines()))
    similarity = (matches / total_lines) * 100 if total_lines > 0 else 0

    return jsonify({"similarity": similarity, "matches": matches})

if __name__ == '__main__':
    app.run(debug=True)
