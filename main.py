
from command import * 
# Setup UI
# Login session (Akun yang login)



# Password DB, dan Database pada Client mySql
dB = DB("aaaaaaaaa","rpl")

# Akun
akun=Akun(dB)

command = Command(akun)




nav="navigasi dengan angka(lihat menu): "
command.header()
user = str(input(nav))
# Hingga user meminta exit
while not(user=='exit'):
  # Pilihan angka
  if (user=='1'):
    # 1 ==> Halaman Login
    # diulang sampai berhasil
    while(akun.loginSession == None):
      command.login()
  elif (user=='2'):
    # 2 ==> Halaman Register, Register berarti sekaligus login
    command.register()
  elif (user=='3'):
    # List semua kendaraan
    command.listKendaraan()
    
    # Navigasi untuk memilih kendaraan
    user = str(input("ketik 'pilih kend []' untuk lebih lengkap: "))
    index=int(user[-1])-1
    
    command.pilihKendaraan(index)
    print("Tampilkan kontak penyewa? Y/N")
    user = input()
    if (user =="Y" or user == "y"):
      command.tampilkanKontak()
  elif (user=='4'):
    # Akun logout, Akun.loginSession menjadi null kembali
    akun.logout()
  elif (user=='5'):
    # REGISTER KENDARAAN, akan di validasi untuk mengarah ke halaman login
    command.regisKendaraan()
  else :
    print("Navigasi angka tidak dikenal\n  ")
  
  command.header()
  user = str(input(nav))
      
