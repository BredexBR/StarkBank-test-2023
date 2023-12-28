from Domain.people import people
import psycopg2

class addPeopleDatabase():
    def addPeopleDatabase(conn, numberRandom):

        print(numberRandom)

        cur = conn.cursor()
        cur.execute(f"SELECT * FROM people where id = {numberRandom} limit 1")
        rows = cur.fetchall()
        for row in rows:
            id = row[0] if row else None
            name = row[1] if row else None
            cpf = row[2] if row else None

        print("name: ", name)

        cur.close()        
        return people(id, name, cpf)
        