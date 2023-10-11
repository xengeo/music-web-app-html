# File: tests/test_album.py

from lib.album import Album

"""Tests the album class"""

"""
Album constructs with 
an id, title, release_year, and artist_id
"""
def test_album_constructs():
    album_1 = Album(1, 'Test Album', 2000, 2)
    assert album_1.id == 1
    assert album_1.title == 'Test Album'
    assert album_1.release_year == 2000
    assert album_1.artist_id == 2


"""
Test we can format albums to strings nicely
"""
def test_albums_format_nicely():
    album_1 = Album(1, 'Test Album', 2000, 2)
    assert str(album_1) == "Album(1, Test Album, 2000, 2)"
    # Try commenting out the `__repr__` method in lib/artist.py
    # And see what happens when you run this test again.


"""
We can compare two identical albums 
and have them be equal
"""
def test_albums_are_equal():
    album_1 = Album(1, 'Test Album', 2000, 2)
    album_2 = Album(1, 'Test Album', 2000, 2)
    assert album_1 == album_2
    # Try commenting out the `__eq__` method in lib/artist.py
    # And see what happens when you run this test again.
