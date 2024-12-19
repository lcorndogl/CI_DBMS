from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)

# executing the instructions from our localhost "chinook" db
db = create_engine('postgresql:///chinook')

meta = MetaData(db)

# create variable for artist table 
artist_table = Table(
    'Artist',
    meta,
    Column('ArtistId', Integer, primary_key=True),
    Column('Name', String)
)

# create variable for album table 
album_table = Table(
    'Album',
    meta,
    Column('AlbumId', Integer, primary_key=True),
    Column('Title', String),
    Column('ArtistId', Integer, ForeignKey('artist_table.ArtistId'))
)

# create variable for track table
track_table = Table(
    'Track',
    meta,
    Column('TrackId', Integer, primary_key=True),
    Column('Name', String),
    Column('AlbumId', Integer, ForeignKey('album_table.AlbumId')),
    Column('MediaTypeId', Integer, ForeignKey("album_table.AlbumId")),
    Column('GenreId', Integer, primary_key=False),
    Column('Composer', String),
    Column('Milliseconds', Integer),
    Column('Bytes', Integer),
    Column('UnitPrice', Float)
)
# making the connection 
with db.connect() as connection:
    
    # Query 1 - select all records from the "Artist" table
    # select_query = artist_table.select()

    # Query 2 - Select only the "Name" column from the "Artist" table 
    # select_query = artist_table.select().with_only_columns([artist_table.c.Name])

    # Query 3 - Select only Queen from the "Artist" table
    # select_query = artist_table.select().where(artist_table.c.Name == "Queen")

    # query 4 - Select only by artist id 51 from the artist table
    # select_query = artist_table.select().where(artist_table.c.ArtistId == 51)


    # query 5 - select only the albums with artistid 51 on the album table
    # select_query = album_table.select().where(album_table.c.ArtistId == 51)

    # query 6 - select tracks where the composer is queen from the track table
    # select_query = track_table.select().where(track_table.c.Composer == "Queen")




    results = connection.execute(select_query)
    for result in results:
        print(result)
