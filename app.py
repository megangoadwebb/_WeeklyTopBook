from flask import Flask, render_template
import requests

app = Flask(__name__)

NYT_API_KEY = 'z2DLoXq6jaHXlyNO6UaXxY27tTQ2Bwak'
NYT_API_URL = 'https://api.nytimes.com/svc/books/v3/lists.json'

def get_best_sellers_list(list_name):
    params = {
        'api-key': NYT_API_KEY,
        'list': list_name
    }
    response = requests.get(NYT_API_URL, params=params)
    if response.status_code == 200:
        return response.json().get('results', [])
    return []

@app.route('/')
def index():
    genres = ['hardcover-fiction', 'hardcover-nonfiction', 'paperback-nonfiction', 'advice-how-to-and-miscellaneous']
    best_sellers = {genre: get_best_sellers_list(genre) for genre in genres}
    return render_template('index.html', best_sellers=best_sellers)

if __name__ == '__main__':
    app.run(debug=True)