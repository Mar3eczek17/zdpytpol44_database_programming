# SQL quries
# SELECT clause (raw sql)

from sqlalchemy import create_engine

conn_string = 'sqlite:///chinook.sqlite'
engine = create_engine(conn_string)

connection = engine.connect()

stmt = 'SELECT * FROM artists'
result_proxy = connection.execute(stmt)  # metoda execute zwraca ResultProxy
results = result_proxy.fetchall() # zwara ResultSet

# print(result_proxy)
print(results)
print(type(results))

first_row = results[0] # LeagcyRaw
print(first_row)
print(type(first_row))
print(dir(first_row))

print(first_row.keys())
print(first_row.values())
print(first_row.ArtistId)
print(first_row.Name)

# Iterujemy po każdym wpisie
for item in results:
    print(item.Name)


# SELECT function

from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import select


# Silnik i napis połączeniowy
conn_string = 'sqlite:///chinook.sqlite'
engine = create_engine(conn_string)

# inicjalizacja połaczenia
connection = engine.connect()

# odbicie tabeli
metadata = MetaData()
artists = Table('artists', metadata, autoload=True, autoload_with=engine)
# zapytania
stmt = select([artists])
print()

results = connection.execute(stmt).fetchall()
print(results)