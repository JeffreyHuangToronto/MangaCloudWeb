import sqlite3
import requests
import json
# required imports; you may add more in the future; currently, we will only use render_template
from flask import Flask, render_template, request, g, session, redirect, url_for, escape, send_file, send_from_directory
# DATABASE = './assignment3.db'


# tells Flask that "this" is the current running app
app = Flask(__name__)
app.secret_key = 'admin'


# setup the default route
# this is the page the site will load by default (i.e. like the home page)


# def get_db():
#     # if there is a database, use it
#     db = getattr(g, '_database', None)
#     if db is None:
#         # otherwise, create a database to use
#         db = g._database = sqlite3.connect(DATABASE)
#     return db

# converts the tuples from get_db() into dictionaries
# (don't worry if you don't understand this code)


# def make_dicts(cursor, row):
#     return dict((cursor.description[idx][0], value)
#                 for idx, value in enumerate(row))

# given a query, executes and returns the result
# (don't worry if you don't understand this code)


# def query_db(query, args=(), one=False):
#     cur = get_db().execute(query, args)
#     rv = cur.fetchall()
#     cur.close()
#     return (rv[0] if rv else None) if one else rv


# @app.teardown_appcontext
# def close_connection(exception):
#     db = getattr(g, '_database', None)
#     if db is not None:
#         # close the database if we are connected to it
#         db.close()

@ app.route('/CompletedManga')
def completed_manga():
    url = "https://mangacloud.azurewebsites.net/api/manga/getcompletedlist?source=MangaKakalot&page=1"
    payload = {}
    headers = {
        'Cookie': 'ARRAffinity=245d3a60ee797bb0440fcba44d0786977f5b4ea366bcd459b9be1921a3a8ea5e; ARRAffinitySameSite=245d3a60ee797bb0440fcba44d0786977f5b4ea366bcd459b9be1921a3a8ea5e'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    return render_template('CompletedManga.html', completed_manga=json.loads(response.text))


@ app.route('/js/<script_name>')
def js(script_name):
    print(script_name)
    return send_from_directory("static", script_name)


@ app.route('/manga/<manga_id>/', methods=["POST", "GET"])
def manga(manga_id):

    # here we want to get the value of user (i.e. ?user=some-value)
    page = request.args.get('page')
    # print(page)
    if page is None:
        url = "https://mangacloud.azurewebsites.net/api/manga/database/searchbyid?manga_id=" + manga_id
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)

        print(response.status_code)
        # if response.status_code == 404:
        return render_template('Manga.html', manga=json.loads(response.text))

    url = "https://mangacloud.azurewebsites.net/api/manga/getpages?manga_id=" + \
        manga_id + "&chapter_number=" + page

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    if response.status_code == 200:
        return render_template('MangaReader.html', manga=json.loads(response.text))


@app.errorhandler(404)
def internal_error(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    return render_template('404.html'), 500


@ app.route('/')
def root():
    url = "https://mangacloud.azurewebsites.net/api/manga/getcompletedlist?source=MangaKakalot&page=1"
    payload = {}
    headers = {
        'Cookie': 'ARRAffinity=245d3a60ee797bb0440fcba44d0786977f5b4ea366bcd459b9be1921a3a8ea5e; ARRAffinitySameSite=245d3a60ee797bb0440fcba44d0786977f5b4ea366bcd459b9be1921a3a8ea5e'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    # print(json.loads(response.text)[0])
    return render_template('index.html')


# https: // mangakakalot.tv/mangaimage /${_id}.jpg
# @ app.route('/remarks', methods=['GET'])


# run the app when app.py is run
if __name__ == '__main__':
    app.run()
