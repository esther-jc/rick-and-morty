from flask import Flask, render_template, url_for, request, redirect, flash, session

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html',
                            title="Rickords")

@app.route('/records/')
def viewRecords():
    return "insert records here"

@app.route('/favorites/')
def viewFavs():
    return render_template('favorites.html',
                            title="Favorites")

@app.route('/map/')
def viewMap():
    return "insert map here"

@app.route('/')
def login():
    return "insert login pop-up modal here"

if __name__ == "__main__":
    app.run(debug=True)