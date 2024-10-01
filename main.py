from flask import Flask, request, jsonify
import wikipediaapi

app = Flask(__name__)

def get_wikipedia_info(subject):
    user_agent = "WikiMi/1.0 (https://github.com/torinwolff/WikiMi)"
    wiki_wiki = wikipediaapi.Wikipedia(language='en', user_agent=user_agent)
    page = wiki_wiki.page(subject)

    if page.exists():
        return {
            "title": page.title,
            "summary": page.summary[:500]  # Return first 500 characters of the summary
        }
    else:
        return {
            "error": f"The page '{subject}' does not exist on Wikipedia."
        }

@app.route('/wiki', methods=['POST'])
def wiki():
    data = request.get_json()
    subject = data.get('subject')
    if not subject:
        return jsonify({"error": "No subject provided"}), 400

    info = get_wikipedia_info(subject)
    return jsonify(info)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8877)