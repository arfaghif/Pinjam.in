from Akun import *
def header(login, akun):
  print("Selamat datang di Pinjam.in")
  if (login):
    print("Halo " + akun.loginSession[0])
    print("3. Lihat Kendaraan")
    print("4. Logout")
    print("5. Register Kendaraan")
  else:
    print("1. Login")
    print("2. Register")
  print("exit. Tinggalkan aplikasi")
    

def login(akun):
  print("Anda Memasuki Halaman Login")
  username = str(input("username: "))
  password = str(input("password: "))
  akun.login(username,password)
  
    # if (Akun.loginSession==None):
    #   print("Login gagal")
    #   user = '1'
    # else:
    #   # Yang ini berhasil, menampilkan tampilan home dan meminta input kembali
    #   header()
    #   user = str(input(nav))


def register(akun):
  print("Anda Memasuki Halaman Register")
  username = str(input("username: "))
  password = str(input("password: "))
  akun.register(username,password)

def listKendaraan(dB):
  kendaraan=[]
  print("Pilihan Kendaraan:")
  dB.getData("Select * from kendaraan", kendaraan)
  for nolist,kend in enumerate(kendaraan,start=1):
    print("{}. {} tahun {} daerah {} by {}".format(nolist, kend[2], kend[3], kend[4], kend[1]))
  return kendaraan


def pilihKendaraan(dB,index,kendaraan):
  obj = {'username':kendaraan[index][1],'nama':kendaraan[index][2],'tahun':kendaraan[index][3],'alamat':kendaraan[index][4],'harga':kendaraan[index][5],'deskripsi':kendaraan[index][6]}      
  print("{} tahun: {} harga sewa/hari: {} alamat: {} deskripsi: {} by {}".format(obj['nama'],obj['tahun'],obj['harga'],obj['alamat'],obj['deskripsi'],obj['username']))
  # Dapat memilih opsi kontak atau kembali ke home setelah pada page kendaraan
  return obj
def regisKendaraan(dB):
  namakend = str(input("Nama Kendaraan: "))
  tahunkend = str(input("Tahun Kendaraan: "))
  alamatkend = str(input("Alamat Kendaraan: "))
  hargakend = int(input("Harga sewa per hari: "))
  deskripsikend = str(input("Masukan Deskripsi Kendaraan: "))
  dB.navigateDatabase("insert into kendaraan (username,namakendaraan,tahun,alamat,harga,deskripsi) values ('{}','{}',{},'{}',{},'{}');".format(Akun.loginSession[0],namakend,tahunkend,alamatkend,hargakend,deskripsikend))
  print("Berhasil meregister kendaraan!")


def tampilkanKontak(dB,obj):
  kontakCurrent=[]
  dB.getData("Select email,no_hp from kontak natural join akun where username='{}'".format(obj['username']), kontakCurrent)
  print("Kontak Pemilik: ")
  print("email: {}".format(kontakCurrent[0][0]))
  print("no hp: {}".format(kontakCurrent[0][1]))