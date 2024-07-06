from flask import Flask, render_template, request
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
        results = response.json().get('results', [])
        if results:
            date = results[0].get('published_date', '')
        else:
            date = ''
        return results, date
    return [], ''

@app.route('/', methods=['GET', 'POST'])
def index():
    genres = ['hardcover-fiction', 'hardcover-nonfiction', 'paperback-nonfiction', 'advice-how-to-and-miscellaneous']
    selected_genre = request.form.get('genre') if request.method == 'POST' else genres[0]
    best_sellers, published_date = get_best_sellers_list(selected_genre)
    return render_template('index.html', genres=genres, best_sellers=best_sellers, selected_genre=selected_genre, published_date=published_date)

if __name__ == '__main__':
    app.run(debug=True)
