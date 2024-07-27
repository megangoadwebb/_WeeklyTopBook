from flask import Flask, render_template, request
import requests
from API_keys import NYT_API_KEY, NYT_API_URL

app = Flask(__name__)

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
    genres = ["combined-print-and-e-book-fiction", "combined-print-and-e-book-nonfiction", "hardcover-fiction", "hardcover-nonfiction", "trade-fiction-paperback", "mass-market-paperback", "paperback-nonfiction", "e-book-fiction", "e-book-nonfiction", "hardcover-advice", "paperback-advice", "advice-how-to-and-miscellaneous", "chapter-books", "childrens-middle-grade", "childrens-middle-grade-e-book", "childrens-middle-grade-hardcover", "childrens-middle-grade-paperback", "paperback-books", "picture-books", "series-books", "young-adult", "young-adult-e-book", "young-adult-hardcover", "young-adult-paperback", "animals", "audio-fiction", "audio-nonfiction", "business-books", "celebrities", "crime-and-punishment", "culture", "education", "espionage", "expeditions-disasters-and-adventures", "fashion-manners-and-customs", "food-and-fitness", "games-and-activities", "graphic-books-and-manga", "hardcover-graphic-books", "health", "humor", "indigenous-americans", "relationships", "mass-market-monthly", "middle-grade-paperback-monthly", "young-adult-paperback-monthly", "hardcover-political-books"]
    selected_genre = request.form.get('genre') if request.method == 'POST' else genres[0]
    best_sellers, published_date = get_best_sellers_list(selected_genre)
    return render_template('index.html', genres=genres, best_sellers=best_sellers, selected_genre=selected_genre, published_date=published_date)

if __name__ == '__main__':
    app.run(debug=True)