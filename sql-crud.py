from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#  Executing the instructions from the "chinook" database 
db = create_engine("postgresql:///chinook")
base = declarative_base()

class Programmer(base):
    __tablename__ = "Programmer"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)

# instead of connecting to the database directly, we will ask for a session 
# create a new instance of sessionmaker, then point to our engine (the db) 
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above 
session = Session()

# create the database using declarative_base subclass 
base.metadata.create_all(db)


# creating records on our Programmer table
ada_lovelace = Programmer(
    first_name = "Ada",
    last_name = "Lovelace",
    gender = "F",
    nationality = "British",
    famous_for = "First Programmer"
)

alan_turing = Programmer(
    first_name = "Alan",
    last_name = "Turing",
    gender = "M",
    nationality = "British",
    famous_for = "Modern Computing"
)

grace_hopper = Programmer(
    first_name = "Grace",
    last_name = "Hopper",
    gender = "F",
    nationality = "American",
    famous_for = "COBOL language"
)

margaret_hamilton = Programmer(
    first_name = "Margaret",
    last_name = "Hamilton",
    gender = "F",
    nationality = "American",
    famous_for = "Apollo 11"
)

bill_gates = Programmer(
    first_name = "Bill",
    last_name = "Gates",
    gender = "M",
    nationality = "American",
    famous_for = "Microsoft"
)

tim_berners_lee = Programmer(
    first_name = "Tim",
    last_name = "Berners-Lee",
    gender = "M",
    nationality = "British",
    famous_for = "World Wide Web"
)

michael_cornall = Programmer(
    first_name = "Michael",
    last_name = "Cornall",
    gender = "M",
    nationality = "British",
    famous_for = "Code Institute Student"
)

# add each instance of our programmers to our session
# session.add(ada_lovelace)
# session.add(alan_turing)
# session.add(grace_hopper)
# session.add(margaret_hamilton)
# session.add(bill_gates)
# session.add(tim_berners_lee)
# session.add(michael_cornall)

# commit our session to the database
# session.commit()

# updating a single record
# programmer = session.query(Programmer).filter_by(id=7).first()
# programmer.famous_for = "World President"

# updating multiple records
# people = session.query(Programmer)
# for person in people:
#     if person.gender == "F":
#         person.gender = "Female"
#     elif person.gender == "M":
#         person.gender = "Male"
#     else:
#         print("Gender not defined")
#     session.commit()

# deleting a single record
fname = input("Enter a first name: ")
lname = input("Enter a last name: ")
programmer=session.query(Programmer).filter_by(first_name=fname, last_name=lname).first()
#defensive programming
# if programmer is not None:
#     print("Programmer found: ", programmer.first_name + " " + programmer.last_name)
#     confirmation = input("Are you sure you want to delete this record? (y/n): ")
#     if confirmation.lower() == "y":
#         session.delete(programmer)
#         session.commit()
#         print("Programmer has been deleted")
#     else:
#         print("Programmer not deleted")
# else:
#     print("No records found")

# deleting multiple records - do not run this unless absolutely sure & perform an input check to ensure that it is what is desired
# programmers = session.query(Programmer)
# for programmer in programmers:
#     session.delete(programmer)
#     session.commit()

# commit our session to the database
session.commit()

# query the database to find all Programmers
programmers = session.query(Programmer)
for programmer in programmers:
    print(
        programmer.id,
        programmer.first_name + " " +programmer.last_name,
        programmer.gender,
        programmer.nationality, 
        programmer.famous_for,
        sep=" | "
    )

# Query 1 - select all records from the "Artist" table 
# artists = session.query(Artist)
# for artist in artists:
#     print(artist.ArtistId, artist.Name, sep=" | ")

# Query 2 - select Name records from the "Artist" table 
# artists = session.query(Artist)
# for artist in artists:
#     print(artist.Name, sep=" | ")


# Query 3 - select "Queen " from "artist"
# artist = session.query(Artist).filter_by(Name="Queen").first()
# print(artist.ArtistId, artist.Name, sep=" | ")

# Query 4 - select "Artist Id #51 " from "artist"
# artist = session.query(Artist).filter_by(ArtistId=51).first()
# print(artist.ArtistId, artist.Name, sep=" | ")

# Query 5 - select only the albums with artistid 51 
# albums = session.query(Album).filter_by(ArtistId=51)
# for album in albums:
#     print(album.AlbumId, album.Title, sep=" | ")

# Query 5 - songs from composer queen 
# tracks = session.query(Track).filter_by(Composer="Queen")
# for track in tracks:
#     print(
#         track.TrackId,
#         track.Name,
#         track.AlbumId,
#         track.MediaTypeId,
#         track.GenreId,
#         track.Composer,
#         track.Milliseconds,
#         track.Bytes,
#         track.UnitPrice,
#         sep=" | "
#     )