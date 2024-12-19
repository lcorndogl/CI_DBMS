import psycopg2


# connect to "chinook" database
connection = psycopg2.connect(database="chinook")

# build a cursor object of the database 
cursor = connection.cursor()


# Query 1 - select all records from the "Artist" table
# cursor.execute('Select * FROM "Artist"')

# query 2 - select only the name column from artists
# cursor.execute('SELECT "Name" FROM "Artist"')

# query 3 - select only queen from the artist table 
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s',["Queen"])

# query 4 - select only by artist id 51 from artist table 
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])

# query 5 select onlt the albums with artistid 51 on the album table 
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])

# query 6 select tracks where the composer is queen from the track table 
# cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Eminem"])

# fetch the results (multiple)
results = cursor.fetchall()

# fetch the results (single)
# results = cursor.fetchone()

# close the connection 
connection.close()

# print results  
for result in results:
    print(result)

