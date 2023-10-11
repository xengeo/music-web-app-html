from playwright.sync_api import Page, expect

# Tests for your routes go here

# Test-drive a GET /albums route that connects with an AlbumRepository and the database to return a result like this:
"""
Test GET /albums returns HTML header tag
"""
def test_get_albums_returns_html_header(page, test_web_address, db_connection):
    db_connection.seed('seeds/music_library.sql')
    page.goto(f'http://{test_web_address}/albums')

    h1_tag = page.locator('h1')
    expect(h1_tag).to_have_text('Albums')


"""
Test GET /albums returns HTML dividers
"""
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

    p_tag = page.locator('p')
    expect(p_tag).to_have_text("Release year: 1989 Artist: Pixies")

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
