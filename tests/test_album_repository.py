import pytest

from lib.album_repository import AlbumRepository
from lib.album import Album


"""
test when we call AlbumRepository#all
We get a list of Artist objects reflecting the seed data
"""
def test_get_all_records(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)
    
    albums = repository.all() # Get all albums

    # Assert on the results
    assert albums == [
        Album(1, 'Doolittle', 1989, 1),
        Album(2, 'Surfer Rosa', 1988, 1),
        Album(3, 'Waterloo', 1974, 2),
        Album(4, 'Super Trouper', 1980, 2),
        Album(5, 'Bossanova', 1990, 1),
        Album(6, 'Lover', 2019, 3),
        Album(7, 'Folklore', 2020, 3),
        Album(8, 'I Put a Spell on You', 1965, 4),
        Album(9, 'Baltimore', 1978, 4),
        Album(10, 'Here Comes the Sun', 1971, 4),
        Album(11, 'Fodder on My Wings', 1982, 4),
        Album(12, 'Ring Ring', 1973, 2)
    ]


"""
Test the find method returns an instance of the artist
object for the specified id
"""
def test_find_returns_specified_album(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)

    album = repository.find(3)

    assert album == Album(3, 'Waterloo', 1974, 2)


# Test-drive a create method for your AlbumRepository class.
# Test-drive a delete method for your AlbumRepository class.

"""
Test when we run AlbumRepository#create with a new user
we can then find that user using AlbumRepository#find
"""
def test_create_can_insert_to_albums_table(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)

    new_album = Album(None, 'New Album Title', 2023, 2)
    repository.create(new_album)

    album = repository.find(13)
    assert album == Album(13, 'New Album Title', 2023, 2)

"""
Test when we run AlbumRepository#delete with a new user
we can then not find that user using AlbumRepository#find
returns error "Album does not exist"
and when we run #all we get the remaining album objects
"""

def test_delete_removes_album(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)

    repository.delete(1)
    
    with pytest.raises(Exception) as err:
        repository.find(1)
        
    assert str(err.value) == "Album ID not found"

    albums = repository.all()
    assert albums == [
        Album(2, 'Surfer Rosa', 1988, 1),
        Album(3, 'Waterloo', 1974, 2),
        Album(4, 'Super Trouper', 1980, 2),
        Album(5, 'Bossanova', 1990, 1),
        Album(6, 'Lover', 2019, 3),
        Album(7, 'Folklore', 2020, 3),
        Album(8, 'I Put a Spell on You', 1965, 4),
        Album(9, 'Baltimore', 1978, 4),
        Album(10, 'Here Comes the Sun', 1971, 4),
        Album(11, 'Fodder on My Wings', 1982, 4),
        Album(12, 'Ring Ring', 1973, 2)
    ]


"""
Test when we delete an album that does not exist
#delete returns an error
"""
def test_delete_nonexistent_album_raises_error(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)

    with pytest.raises(Exception) as err:
        repository.delete(20)
    assert str(err.value) == "Album ID not found"