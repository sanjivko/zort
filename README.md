# zort
The aim is to generate C++ classes representing database tables. The input to the script is a database dump file generated from pg_dump. 
Will try out for psql dumps and then implement for other database types.


Command:
./gen.py <input-db-file-name>

e.g
> ./gen.py dbFile.sql 
