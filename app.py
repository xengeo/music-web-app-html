import os
from flask import Flask, request, render_template, redirect
from lib.database_connection import get_flask_database_connection
from lib.album import Album
from lib.album_repository import AlbumRepository
from lib.artist import Artist
from lib.artist_repository import ArtistRepository
from lib.album_parameter_validator import is_valid

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# ========= ALBUMS ==========
@app.route('/albums/new', methods=['GET']) # GET is the default
def get_album_new():
    return render_template("albums/new.html")    


@app.route('/albums/<int:id>', methods=['GET'])
def single_album(id):
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    album = repository.get_with_artist(id)
    return render_template('albums/show.html', album=album) # have to specify arg name i.e. like keyword arg


@app.route('/albums', methods=['POST', 'GET'])
def albums():

    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)

    # POST REQUEST
    if request.method == 'POST':

        title = request.form['title']
        release_year = request.form['release_year']

        new_album = Album(None, title, release_year, 2)

        if not is_valid(new_album):
            return render_template("albums/new.html", errors="Album title and/or release year inputs were invalid")
        
        repository.create(new_album)

        return redirect(f"/albums/{new_album.id}")
    
    # GET REQUEST
    if request.method == 'GET':
        albums = repository.all()
        return render_template('albums/index.html', albums=albums)


# ========= ARTISTS ==========
@app.route('/artists/new', methods=['GET']) # GET is the default
def get_artist_new():
    return render_template("artists/new.html")  


@app.route('/artists/<int:id>', methods=['GET'])
def single_artist(id):
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artist = repository.find(id)
    return render_template('artists/show.html', artist=artist) # have to specify arg name i.e. like keyword arg


@app.route('/artists', methods=['GET', 'POST'])
def artists():

    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    
    # GET REQUEST
    if request.method == 'GET':
        artists = repository.all()
        return render_template('artists/index.html', artists=artists)

    # POST REQUEST
    if request.method == 'POST':
        
        name = request.form['name']
        genre = request.form['genre']

        artist = Artist(None, name, genre)

        # if not is_valid(new_album):
        #     return render_template("albums/new.html", errors="Album title and/or release year inputs were invalid")
        
        repository.create(artist)
        print(artist)
        return redirect(f"/artists/{artist.id}")














# == Example Code Below ==

# GET /emoji
# Returns a smiley face in HTML
# Try it:
#   ; open http://localhost:5001/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    # We use `render_template` to send the user the file `emoji.html`
    # But first, it gets processed to look for placeholders like {{ emoji }}
    # These placeholders are replaced with the values we pass in as arguments
    return render_template('emoji.html', emoji=':)')

# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
