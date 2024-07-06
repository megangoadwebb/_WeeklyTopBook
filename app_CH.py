from flask import Flask, render_template, request
import requests
import time

app = Flask(__name__)

from API_keys import NYT_API_KEY 
# you will need to create a file called API_keys.py in the same directory as this file with this in it:
# NYT_API_KEY = 'your_key_here'
NYT_API_URL = 'https://api.nytimes.com/svc/books/v3/lists.json'
def get_best_sellers_list(list_name):
    params = {
        'api-key': NYT_API_KEY,
        'list': list_name
    }
    num_tries = 5
    while num_tries > 0:
        response = requests.get(NYT_API_URL, params=params)
        if response.status_code == 200:
            return response.json().get('results', [])
        time.sleep(1)
        num_tries -= 1
    return []

@app.route('/')
def index():
    selected_genre = request.args.get('genre', 'all') # if no genre is give then default is 'all'
    genres = ['hardcover-fiction', 'hardcover-nonfiction', 'paperback-nonfiction', 'advice-how-to-and-miscellaneous']
    best_sellers = {}
    if selected_genre == 'all':
        for genre in genres:
            best_sellers[genre] = get_best_sellers_list(genre)
    else:
        best_sellers[selected_genre] = get_best_sellers_list(selected_genre)

    html = render_template('index2.html', best_sellers=best_sellers, genres=genres)
    return html

if __name__ == '__main__':
    app.run(debug=False)