from Akun import *
class Command :
  def __init__(self, akun):
    self.akun = akun
    self.kendaraan = None
    self.obj = None
  def header(self):
    print("Selamat datang di Pinjam.in")
    if (self.akun.loginSession != None):
      print("Halo " + self.akun.loginSession[0])
      print("3. Lihat Kendaraan")
      print("4. Logout")
      print("5. Register Kendaraan")
    else:
      print("1. Login")
      print("2. Register")
    print("exit. Tinggalkan aplikasi")
      

  def login(self):
    print("Anda Memasuki Halaman Login")
    username = str(input("username: "))
    password = str(input("password: "))
    self.akun.login(username,password)
    
      # if (Akun.loginSession==None):
      #   print("Login gagal")
      #   user = '1'
      # else:
      #   # Yang ini berhasil, menampilkan tampilan home dan meminta input kembali
      #   header()
      #   user = str(input(nav))


  def register(self):
    print("Anda Memasuki Halaman Register")
    username = str(input("username: "))
    password = str(input("password: "))
    self.akun.register(username,password)

  def listKendaraan(self):
    self.kendaraan=[]
    print("Pilihan Kendaraan:")
    self.akun.getDatabase().getData("Select * from kendaraan", self.kendaraan)
    for nolist,kend in enumerate(self.kendaraan,start=1):
      print("{}. {} tahun {} daerah {} by {}".format(nolist, kend[2], kend[3], kend[4], kend[1]))


  def pilihKendaraan(self,index):
    self.obj = {'username':self.kendaraan[index][1],'nama':self.kendaraan[index][2],'tahun':self.kendaraan[index][3],'alamat':self.kendaraan[index][4],'harga':self.kendaraan[index][5],'deskripsi':self.kendaraan[index][6]}      
    print("{} tahun: {} harga sewa/hari: {} alamat: {} deskripsi: {} by {}".format(self.obj['nama'],self.obj['tahun'],self.obj['harga'],self.obj['alamat'],self.obj['deskripsi'],self.obj['username']))
    # Dapat memilih opsi kontak atau kembali ke home setelah pada page kendaraan
  def regisKendaraan(self):
    namakend = str(input("Nama Kendaraan: "))
    tahunkend = str(input("Tahun Kendaraan: "))
    alamatkend = str(input("Alamat Kendaraan: "))
    hargakend = int(input("Harga sewa per hari: "))
    deskripsikend = str(input("Masukan Deskripsi Kendaraan: "))
    self.akun.getDatabase().navigateDatabase("insert into kendaraan (username,namakendaraan,tahun,alamat,harga,deskripsi) values ('{}','{}',{},'{}',{},'{}');".format(self.akun.loginSession[0],namakend,tahunkend,alamatkend,hargakend,deskripsikend))
    print("Berhasil meregister kendaraan!")


  def tampilkanKontak(self):
    kontakCurrent=[]
    self.akun.getDatabase().getData("Select email,no_hp from kontak natural join akun where username='{}'".format(self.obj['username']), kontakCurrent)
    print("Kontak Pemilik: ")
    print("email: {}".format(kontakCurrent[0][0]))
    print("no hp: {}".format(kontakCurrent[0][1]))