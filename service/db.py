import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="mentari",
        database="db_solusiku"
    )

def cek_username(username):
    try:
        conn = get_connection()
        cursor = conn.cursor(buffered=True)
        query = "SELECT COUNT(*) FROM data_user WHERE username = %s"
        cursor.execute(query, (username,))
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return result[0] > 0
    except mysql.connector.Error as e:
        print("Database error:", e)
        return False

def insert_user(username, password, jenis_pertanyaan, jwb_pertanyaan='', alamat='', no_telp='', nama=''):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = """
        INSERT INTO data_user (username, password, jenis_pertanyaan, jwb_pertanyaan, alamat, no_telp, nama)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (username, password, jenis_pertanyaan, jwb_pertanyaan, alamat, no_telp, nama))
        conn.commit()
        cursor.close()
        conn.close()
        print(f"User {username} berhasil disimpan")
    except mysql.connector.Error as e:
        print("Database error:", e)
