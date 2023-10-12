from lib.album import Album
from lib.album_parameter_validator import is_valid


"""
Test validate inputs for invalid album
Returns False
"""
def test_validate_invalid_album():
    invalid_album = Album(1, '', '', 1)
    assert is_valid(invalid_album) == False

"""
Test validate inputs for invalid album
Returns False
"""
def test_validate_valid_album():
    invalid_album = Album(1, 'AlbumTitle', '2002', 1)
    assert is_valid(invalid_album) == True