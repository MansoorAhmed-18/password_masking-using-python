import pymysql #pymsql or mysql connector python both are same
from password_utils import get_decrypted_password

def connect_to_mysql():
    conn= pymysql.connect(
        host="localhost",
        user="root",
        password=get_decrypted_password(),
        database="mysql"
    )

    print("connected to mysql successfully")
    print(get_decrypted_password())


    cursor = conn.cursor()
    cursor.execute("select * from employees")
    print(cursor.fetchall())
    conn.close()

if __name__ == "__main__":
    connect_to_mysql()
