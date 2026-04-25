import psycopg2

def create_connection():
    try:
        connection = psycopg2.connect(dbname="mygaragelite_dev", user="postgres", host="localhost", password="PSALMS")
        return connection
    except Exception as e:
        print(e)
        return None
    

def save_vehicle_db(year, make, model, mileage):
    connection = create_connection()

    if connection:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO vehicles(year, make, model, mileage) VALUES(%s, %s, %s, %s) RETURNING id", (year, make, model, mileage))
        new_id = cursor.fetchone()[0]
        connection.commit()
        connection.close()
        print("vehicle saved successfully!")
        return new_id
    else:
        print("failed")
        return None
    
def update_vehicle_db(vehicle_id, year, make, model, mileage):
    connection = create_connection()

    if connection:
        cursor = connection.cursor()
        cursor.execute("UPDATE vehicles SET year = %s, make = %s, model = %s, mileage = %s WHERE id = %s", (year, make, model, mileage, vehicle_id))
        connection.commit()
        connection.close()
    else:
        print("Update failed")
        return None
    
def delete_vehicle_db(vehicle_id):
    connection = create_connection()

    if connection:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM vehicles WHERE id = %s;", (vehicle_id,))
        connection.commit()
        connection.close()
    else:
        print("Deletion failed")



def load_vehicle_db():
    connection = create_connection()

    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM vehicles ORDER BY id;")
        rows = cursor.fetchall()
        connection.close()
        return rows
    else:
        return []
    

