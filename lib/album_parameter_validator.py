# File: tests/album_parameter_validator.py

from lib.album import Album

"""
Module containing simple function to test album title and release year for validity
"""

def is_valid(album:Album):

    if album.title in [None, ''] or album.release_year in [None, '']:
        return False
    return True