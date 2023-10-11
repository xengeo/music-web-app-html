import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from lib.album import Album
from lib.album_repository import AlbumRepository
from lib.artist import Artist
from lib.artist_repository import ArtistRepository

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# == Your Routes Here ==
@app.route('/albums', methods=['POST', 'GET'])
def albums():

    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)

    if request.method == 'POST':
        title = request.form.get('title')
        release_year = request.form.get('release_year')
        artist_id = request.form.get('artist_id')

        new_album = Album(None, title, release_year, artist_id)
        repository.create(new_album)
        return ''
    
    if request.method == 'GET':
        albums = repository.all()
        return render_template('albums.html', albums=albums)

@app.route('/artists', methods=['GET', 'POST'])
def artists():

    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    
    # GET REQUEST
    if request.method == 'GET':
        artists = repository.all()
        return ', '.join(artist.name for artist in artists)

    # POST REQUEST
    if request.method == 'POST':
        
        if 'name' not in request.form or 'genre' not in request.form:
            return 'You must provide an artist name and genre parameter', 400

        name = request.form['name']
        genre = request.form['genre']

        new_artist = Artist(None, name, genre)
        repository.create(new_artist)

        return ''

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
