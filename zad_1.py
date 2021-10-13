# Zaimportuj funkcję create_engine
from sqlalchemy import create_engine

# Stwórz silnik do bazy sqlite (pliku) census.sqlite
conn_string = 'sqlite:///chinook.sqlite'
engine = create_engine(conn_string)

# Wyświetl nazwy tabel znajdujących się w bazie census.sqlite
print(engine.table_names())
