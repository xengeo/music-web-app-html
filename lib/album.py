
class Album:
    # We initialise with all of our attributes
    # Each column in the table should have an attribute here
    def __init__(self, id, title, release_year, artist_id, artist_name = None):
        self.id = id
        self.title = title
        self.release_year = release_year
        self.artist_id = artist_id
        self.artist_name = artist_name

    # This method allows our tests to assert that the objects it expects
    # are the objects we made based on the database records.
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    # This method makes it look nicer when we print an Artist
    def __repr__(self):

        if self.artist_name:
            return f"Album({self.id}, {self.title}, {self.release_year}, {self.artist_id}, {self.artist_name})"
        return f"Album({self.id}, {self.title}, {self.release_year}, {self.artist_id})"