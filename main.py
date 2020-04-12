from command import * 

# Password DB, dan Database pada Client mySql

dB = DB("afterlife86","rpl")


# Akun
akun=Akun(dB)
command = Command(akun)

# Setup UI
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
    print("Tampilkan kontak penyewa? Y/N : Tampilkan kontak dan Lanjutkan Penawaran")
    user = input()
    if (user =="Y" or user == "y"):
      command.tampilkanKontak()
    print("Ajukan Penawaran? Y/N")
    user = input()
    if (user =="Y" or user == "y"):
      command.nominalPenawaran()
  elif (user=='4'):
    # Akun logout, Akun.loginSession menjadi null kembali
    akun.logout()
  elif (user=='5'):
    # REGISTER KENDARAAN, akan di validasi untuk mengarah ke halaman login
    command.regisKendaraan()
  elif (user=='6'):
    command.daftarTransaksi()
  elif ('konfirmasi' in user):
    command.konfirmasiPenawaran()
    command.daftarTransaksi()
  elif (user=='7'):
    print("Anda yakin menjadi penyewa? Y/N")
    user=input()
    if (user =="Y" or user == "y"):
      command.jadiPenyewa()
  elif (user=='8'):
    ada=command.cariKendaraan()
    if (ada==True):
      user = str(input("ketik 'pilih kend []' untuk lebih lengkap: "))
      index=int(user[-1])-1
      command.pilihKendaraan(index)
      print("Tampilkan kontak penyewa? Y/N : Tampilkan kontak dan Lanjutkan Penawaran")
      user = input()
      if (user =="Y" or user == "y"):
        command.tampilkanKontak()
      print("Ajukan Penawaran? Y/N")
      user = input()
      if (user =="Y" or user == "y"):
        command.nominalPenawaran()
  elif (user=='9'):
    command.beriUlasan()
  else :
    print("Navigasi angka tidak dikenal\n  ")
  
  command.header()
  user = str(input(nav))
      
