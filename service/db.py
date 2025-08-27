import mysql.connector

def cek_username(username):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="mentari",
        database="db_solusiku"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM data_user WHERE username = %s", (username,))
    result = cursor.fetchone()[0]
    cursor.close() 
    conn.close() 
    return result > 0



"""
#Insert Data User (Register)
def insert_register(username, password, jenis_pertanyaan, jwb_pertanyaan):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO data_user(username, password, jenis_pertanyaan, jwb_pertanyaan) VALUES (%s, %s, %s, %s)", (username, password, jenis_pertanyaan, jwb_pertanyaan))
    conn.commit()
    cursor.close() #menutup cursor setelah menjalankan query
    conn.close() #menutup koneksi ke MySQL
"""