
from console import * 
# Setup UI
# Login session (Akun yang login)



# Password DB, dan Database pada Client mySql
dB = DB("aaaaa","rpl")

# Akun
akun=Akun(dB)




nav="navigasi dengan angka(lihat menu): "
header(akun.loginSession !=None,akun)
user = str(input(nav))
# Hingga user meminta exit
while not(user=='exit'):
  # Pilihan angka
  if (user=='1'):
    # 1 ==> Halaman Login
    # diulang sampai berhasil
    while(akun.loginSession == None):
      login(akun)
  elif (user=='2'):
    # 2 ==> Halaman Register, Register berarti sekaligus login
    register(akun)
  elif (user=='3'):
    # List semua kendaraan
    kendaraan = listKendaraan(dB)
    
    # Navigasi untuk memilih kendaraan
    user = str(input("ketik 'pilih kend []' untuk lebih lengkap: "))
    index=int(user[-1])-1
    
    obj = pilihKendaraan(dB,index,kendaraan)
    print("Tampilkan kontak penyewa? Y/N")
    user = input()
    if (user =="Y" or user == "y"):
      tampilkanKontak(dB,obj)
  elif (user=='4'):
    # Akun logout, Akun.loginSession menjadi null kembali
    akun.logout()
  elif (user=='5'):
    # REGISTER KENDARAAN, akan di validasi untuk mengarah ke halaman login
    regisKendaraan(dB)
  else :
    print("Navigasi angka tidak dikenal\n  ")
  
  header(akun.loginSession !=None,akun)
  user = str(input(nav))
      
