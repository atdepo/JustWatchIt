from flask import Flask, render_template, request
from dataCleaning import main_proc
import query_manager as query
import json

app = Flask(__name__)


@app.route('/')
def hello_world():
    # return main_proc()
    return render_template('/index.html')


@app.route("/query/find_by_type", methods=['POST'])
def find_by_type():
    if request.method == 'POST':
        name = request.form['type']
        results = query.filter_by_type(name)
        return render_template('/query.html', results=results, size=len(results),
                               title="Ricerca per tipologia: " + name)
    return json.dumps({"ok": True})


@app.route("/query/show_update", methods=['POST'])
def show_update():
    title = request.form["title"]

    res = query.find_by_title_equals(title=title)
    return render_template('/update.html', element=res)


@app.route("/query/find_by_genre", methods=['POST'])
def find_by_genre():
    if request.method == 'POST':
        genre = request.form['genre']
        results = query.find_by_genres(genre)
        return render_template('/query.html', results=results, size=len(results),
                               title="Ricerca per genere: " + genre)
    return json.dumps({"ok": True})


@app.route("/query/find_by_title", methods=['POST'])
def find_by_title():
    if request.method == 'POST':
        title = request.form['title']
        results = query.find_by_title(title)
        return render_template('/query.html', results=results, size=len(results),
                               title="Ricerca per titolo: " + title)
    return json.dumps({"ok": True})


@app.route("/query/find_by_year", methods=['POST'])
def find_by_year():
    if request.method == 'POST':
        year = request.form['year']
        results = query.find_by_year(year)
        return render_template('/query.html', results=results, size=len(results), title="Ricerca per anno: " + year)
    return json.dumps({"ok": True})


@app.route("/query/find_by_year_range", methods=['POST'])
def find_by_year_range():
    if request.method == 'POST':
        min = request.form['min_year']
        max = request.form['max_year']
        results = query.find_by_year_range(min, max)
        return render_template('/query.html', results=results, size=len(results),
                               title="Ricerca tra: " + min + " e " + max)
    return json.dumps({"ok": True})


@app.route("/query/find_by_director", methods=['POST'])
def find_by_director():
    if request.method == 'POST':
        director = request.form['director']
        results = query.find_by_director(director)
        return render_template('/query.html', results=results, size=len(results),
                               title="Ricerca per regista: " + director)
    return json.dumps({"ok": True})


@app.route("/query/find_series_by_at_least_season_count", methods=['POST'])
def find_series_by_at_least_season_count():
    if request.method == 'POST':
        seasons = request.form['seasons']
        results = query.find_series_by_at_least_season_count(seasons)
        return render_template('/query.html', results=results, size=len(results),
                               title="Ricerca per numero di stagioni: " + seasons)
    return json.dumps({"ok": True})


@app.route("/query/find_by_rating", methods=['POST'])
def find_by_rating():
    if request.method == 'POST':
        rating = request.form['rating']
        results = query.find_by_rating(rating)
        return render_template('/query.html', results=results, size=len(results),
                               title="Ricerca per numero di stagioni: " + rating)
    return json.dumps({"ok": True})


@app.route("/query/find_orderby_date", methods=['POST'])
def find_orderby_date():
    if request.method == 'POST':
        order = request.form['order']
        limit = int(request.form['limit'])
        page = int(request.form['page'])
        results = query.find_orderby_date_limited(order, limit, page)
        ordination = "decrescente" if order == 1 else "decrescente"
        return render_template('/query.html', results=results, size=len(results),
                               title="Ricerca ordinata per anno di uscita " + ordination)
    return json.dumps({"ok": True})


if __name__ == '__main__':
    app.run()
