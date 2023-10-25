import sqlite3

artist = input()

conn = sqlite3.connect("music_db.sqlite")
cursor = conn.cursor()
get_artist_id = f"""
    SELECT ArtistId
    FROM Artist
    WHERE Name = '{artist}';
    """
artists = cursor.execute(get_artist_id).fetchone()
albums = []

get_album_id = f"""
    SELECT AlbumId
    FROM Album
    WHERE ArtistId = {artists[0]};
    """
albums.extend(cursor.execute(get_album_id).fetchall())
tracks = []
for i in albums:
    get_track_id = f"""
            SELECT DISTINCT Name
            FROM Track
            WHERE AlbumId = {i[0]};
            """
    tracks.extend(cursor.execute(get_track_id).fetchall())
unique_tracks = list(set(tracks))
for row in sorted(unique_tracks):
    print(row[0])

conn.close()
