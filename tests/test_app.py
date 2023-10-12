import pytest
from playwright.sync_api import Page, expect

# Tests for your routes go here

# Test-drive a GET /albums route that connects with an AlbumRepository and the database to return a result like this:
"""
Test GET /albums returns HTML header tag
"""
@pytest.mark.skip
def test_get_albums_returns_html_header(page, test_web_address, db_connection):
    db_connection.seed('seeds/music_library.sql')
    page.goto(f'http://{test_web_address}/albums')

    h1_tag = page.locator('h1')
    expect(h1_tag).to_have_text('Albums')


"""
Test GET /albums returns HTML dividers
"""
@pytest.mark.skip
def test_get_albums_returns_html_albums(page, test_web_address, db_connection):
    db_connection.seed('seeds/music_library.sql')
    page.goto(f'http://{test_web_address}/albums')

    h1_tag = page.locator('div')
    expect(h1_tag).to_have_text([
        'Title: Doolittle\nReleased: 1989',
        'Title: Surfer Rosa\nReleased: 1988'
    ])


#GET /albums/1
"""
Test GET /albums/1 with specific album id
Return HTML with info for single album
"""
def test_get_album_with_id(page, test_web_address, db_connection):
    db_connection.seed('seeds/music_library.sql')
    page.goto(f'http://{test_web_address}/albums/1')
    h1_tag = page.locator('h1')
    expect(h1_tag).to_have_text("Doolittle")

    p_tag = page.locator('.t-year-artist')
    expect(p_tag).to_have_text("Release year: 1989 Artist: Pixies")


"""
Test GET /albums returns a page containing links for each
album
"""
def test_get_albums_contains_album_links(page, test_web_address, db_connection):
    db_connection.seed('seeds/music_library.sql')
    page.goto(f"http://{test_web_address}/albums")
    a_tag = page.locator('a')
    expect(a_tag).to_have_text([
        "Doolittle", "Surfer Rosa", "Waterloo", "Super Trouper",
        "Bossanova", "Lover", "Folklore", "I Put a Spell on You",
        "Baltimore", "Here Comes the Sun", "Fodder on My Wings", 
        "Ring Ring"
    ])


"""
Test GET /albums can navigate to GET albums/<id> route via clicking links
"""
def test_get_albums_navigate_to_album_page(page, test_web_address, db_connection):
    db_connection.seed('seeds/music_library.sql')
    page.goto(f"http://{test_web_address}/albums")
    page.click("text=Lover")
    p_tag = page.locator(".t-year-artist")
    expect(p_tag).to_have_text("Release year: 2019 Artist: Taylor Swift")


"""
Test GET /albums can navigate to GET albums/<id> route and back
"""
def test_get_albums_navigate_to_album_page_and_back(page, test_web_address, db_connection):
    db_connection.seed('seeds/music_library.sql')
    page.goto(f"http://{test_web_address}/albums")
    page.click("text=Lover")
    page.click("text=Back to all albums")
    a_tag = page.locator('a')
    expect(a_tag).to_have_text([
        "Doolittle", "Surfer Rosa", "Waterloo", "Super Trouper",
        "Bossanova", "Lover", "Folklore", "I Put a Spell on You",
        "Baltimore", "Here Comes the Sun", "Fodder on My Wings", 
        "Ring Ring"
    ])

# CHALLENGE:

    # Add a route GET /artists/<id> which returns 
    # an HTML page showing details for a single artist.

    # Add a route GET /artists which returns an HTML page with the list of artists. 
    # This page should contain a link for each artist listed, 
    # linking to /artists/<id> where <id> needs to be the corresponding artist id.

#GET /artists/1
"""
Test GET /artists/1 with specific artist id
Return HTML with info for single artist
"""
def test_get_artist_with_id(page, test_web_address, db_connection):

    db_connection.seed('seeds/music_library.sql')
    page.goto(f'http://{test_web_address}/artists/1')

    h1_tag = page.locator('h1')
    expect(h1_tag).to_have_text("Pixies")

    p_tag = page.locator('.t-genre')
    expect(p_tag).to_have_text("Genre: Rock")



"""
Test GET /artists returns a page containing links for each
artist
"""
def test_get_artists_contains_artist_links(page, test_web_address, db_connection):
    db_connection.seed('seeds/music_library.sql')
    page.goto(f"http://{test_web_address}/artists")
    a_tag = page.locator('a')
    expect(a_tag).to_have_text([
        "Pixies", "ABBA", "Taylor Swift", "Nina Simone"
    ])


"""
Test GET /artists can navigate to GET artists/<id> route and back
"""
def test_get_artists_navigate_to_artist_page_and_back(page, test_web_address, db_connection):
    db_connection.seed('seeds/music_library.sql')
    page.goto(f"http://{test_web_address}/artists")

    page.click("text=ABBA")
    p_tag = page.locator('.t-genre')
    expect(p_tag).to_have_text("Genre: Pop")

    page.click("text=Back to all artists")
    a_tag = page.locator('a')
    expect(a_tag).to_have_text([
        "Pixies", "ABBA", "Taylor Swift", "Nina Simone"
    ])











# === Example Code Below ===

"""
We can get an emoji from the /emoji page
"""
def test_get_emoji(page, test_web_address): # Note new parameters
    # We load a virtual browser and navigate to the /emoji page
    page.goto(f"http://{test_web_address}/emoji")

    # We look at the <strong> tag
    strong_tag = page.locator("strong")

    # We assert that it has the text ":)"
    expect(strong_tag).to_have_text(":)")

# === End Example Code ===
