from dotenv import load_dotenv
import os
import psycopg2

load_dotenv()


def create_connection():
    try:
        connection = psycopg2.connect(dbname=os.getenv("DB_NAME"), 
                                      user=os.getenv("DB_USER"), 
                                      password=os.getenv("DB_PASSWORD"), 
                                      host=os.getenv("DB_HOST"), 
                                      port=os.getenv("DB_PORT")
                                      )

        return connection
    except Exception as e:
        print("DB CONNECTION FAILED:", e)
        return None

def save_vehicle_db(year, make, model, mileage):
    connection = None
    try:
        connection = create_connection()

        if not connection:
            print("Save vehicle failed")
            return None


        cursor = connection.cursor()
        cursor.execute("INSERT INTO vehicles(year, make, model, mileage) VALUES(%s, %s, %s, %s) RETURNING id", (year, make, model, mileage))
        new_id = cursor.fetchone()[0]
        connection.commit()
        return new_id
        
    except Exception as e:

        if connection:
            connection.rollback()

        print("Save vehicle failed:", e)
        return False
    
    finally:
        if connection:
            connection.close()


def update_vehicle_db(vehicle_id, year, make, model, mileage):
    connection = None

    try:
        connection = create_connection() 

        if not connection:
            print("Update failed")
            return False
        
        cursor = connection.cursor()
        cursor.execute("UPDATE vehicles SET year = %s, make = %s, model = %s, mileage = %s WHERE id = %s", (year, make, model, mileage, vehicle_id))
        connection.commit()
        return True
        
    except Exception as e:

        if connection:
            connection.rollback()

        print("Update vehicle failed:", e)
        return False
    
    finally:
        if connection:
            connection.close()


def delete_vehicle_db(vehicle_id):
    connection = None

    try:
        connection = create_connection()

        if not connection:
            print("Deletion failed")
            return False
            
        cursor = connection.cursor()
        cursor.execute("DELETE FROM vehicles WHERE id = %s;", (vehicle_id,))
        connection.commit()
        return True

    except Exception as e:

        if connection:
            connection.rollback()
        
        print("Delete vehicle failed:", e)

        return False
    
    finally:
        if connection:
            connection.close()



def load_vehicle_db():
    connection = None

    try:
        connection = create_connection()

        if not connection:
            return []

        cursor = connection.cursor()
        cursor.execute("SELECT * FROM vehicles ORDER BY id;")
        rows = cursor.fetchall()
        return rows        
        
    except Exception as e:
        print("Load vehicle failed", e)
        return []

    finally:
        if connection:
            connection.close()
