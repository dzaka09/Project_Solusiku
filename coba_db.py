from service.db import cek_username

print("*******CHECK USERNAME*******\n")
username = input("Masukkan Username : ")
    
    
    
def check_username(username):
    print("\n")
    if cek_username(username) == True:
        print("Mohon maaf, username tidak tersedia")
    else:
        print("Lanjut, username masih tersedia") 
       
if len(username) > 0:
    check_username(username)        