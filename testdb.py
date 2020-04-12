import mysql.connector

class DB:
  def __init__(self, password, database):
    self.database = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd=password,
      database=database
    )
    self.cursor = self.database.cursor()

  def navigateDatabase(self,query):
    self.cursor.execute(query)
    # for el in self.cursor:
    #   print(el)

  def getData(self,query,data):
    self.cursor.execute(query)
    self.queryResult(data)
  
  def insertDatabase(self,query,val):
    self.cursor.execute(query,val)
    self.database.commit()

  def queryResult(self,data):
    for el in self.cursor:
      data.append(el)
    return data
  
class Akun:
  def __init__(self, database):
    self.loginSession=None
    self.database=database
    self.account=[]
    self.getAccount()
  
  def getAccount(self):
    self.database.getData("select username,password from akun", self.account)

  def register(self, username, password):
    if (self.loginSession==None):
      sql = "INSERT INTO akun (username, password) VALUES (%s, %s)"
      val = (username, password)
      self.database.insertDatabase(sql,val)
      print("Berhasil register")
      # print(self.database.cursor.rowcount, "record inserted.")
      self.getAccount()
      self.login(username, password)
    else:
      print("logout terlebih dahulu")
  
  def login(self,username,password):
    if (self.loginSession==None):
      for key,val in self.account:
        if (username==key):
          if (password==val):
            self.loginSession = (key, val)
            # print(self.loginSession)
            print("Login Berhasil")
          else:
            print("password salah")
    else:
      print("logout terlebih dahulu")

  def logout(self):
    self.loginSession=None


# Password DB, dan Database pada Client mySql

DB = DB("aaaaaaaa","rpl")

# Akun
Akun=Akun(DB)


# Setup UI
# Login session (Akun yang login)
def header():
  print("Selamat datang di Pinjam.in")
  if not (Akun.loginSession==None):
    print("Halo " + Akun.loginSession[0])
    print("3. Lihat Kendaraan")
    print("4. Logout")
    print("5. Register Kendaraan")
  else:
    print("1. Login")
    print("2. Register")
    print("3. Lihat Kendaraan")
    print("5. Register Kendaraan")

nav="navigasi dengan angka(lihat menu): "
header()
user = str(input(nav))
# Hingga user meminta exit
while not(user=='exit'):
  # Pilihan angka
  if (user=='1'):
    # 1 ==> Halaman Login
    print("Anda Memasuki Halaman Login")
    username = str(input("username: "))
    password = str(input("password: "))
    Akun.login(username,password)
    # Login gagal (Current akun / login session masih null / none)
    if (Akun.loginSession==None):
      print("Login gagal")
      user = '1'
    else:
      # Yang ini berhasil, menampilkan tampilan home dan meminta input kembali
      header()
      user = str(input(nav))
  elif (user=='2'):
    # 2 ==> Halaman Register, Register berarti sekaligus login
    print("Anda Memasuki Halaman Register")
    username = str(input("username: "))
    password = str(input("password: "))
    Akun.register(username,password)
    # Menampilkan home setelah berhasil regis dan otomatis login
    header()
    user = str(input(nav))
  elif (user=='3'):
    # List semua kendaraan
    kendaraan=[]
    print("Pilihan Kendaraan:")
    DB.getData("Select * from kendaraan", kendaraan)
    for nolist,kend in enumerate(kendaraan,start=1):
      print("{}. {} tahun {} daerah {} by {}".format(nolist, kend[2], kend[3], kend[4], kend[1]))
    # Navigasi untuk memilih kendaraan
    user = str(input("ketik 'pilih kend []' untuk lebih lengkap: "))
  elif (user=='4'):
    # Akun logout, Akun.loginSession menjadi null kembali
    Akun.logout()
    # Home kembali
    header()
    user = str(input(nav))
  elif ('pilih' in user):
      # Navigasi memilih kendaraan, dan membuka page kendaraan tersebut
      index=int(user[-1])-1
      obj = {'username':kendaraan[index][1],'nama':kendaraan[index][2],'tahun':kendaraan[index][3],'alamat':kendaraan[index][4],'harga':kendaraan[index][5],'deskripsi':kendaraan[index][6]}      
      print("{} tahun: {} harga sewa/hari: {} alamat: {} deskripsi: {} by {}".format(obj['nama'],obj['tahun'],obj['harga'],obj['alamat'],obj['deskripsi'],obj['username']))
      # Dapat memilih opsi kontak atau kembali ke home setelah pada page kendaraan
      print("6. Kontak Penyewa")
      print("7. Kembali ke home")
      user = str(input(nav))
  elif (user=='6'):
    # Menampilkan Kontak
    kontakCurrent=[]
    DB.getData("Select email,no_hp from kontak natural join akun where username='{}'".format(obj['username']), kontakCurrent)
    print("Kontak Pemilik: ")
    print("email: {}".format(kontakCurrent[0][0]))
    print("no hp: {}".format(kontakCurrent[0][1]))
    # Opsi melihat kendaraan, atau balik ke home 
    print("3. Kembali melihat kendaraan")
    print("7. Kembali ke home")
    user = str(input(nav))
  elif (user=='7'):
    # HOME
    header()
    user = str(input(nav))
  elif (user=='5'):
    # REGISTER KENDARAAN, akan di validasi untuk mengarah ke halaman login
    if (Akun.loginSession==None):
      # Harus Login dahulu, (loginSession == NULL), untuk itu di arahkan menuju login atau ke balik ke home
      print("Login terlebih dahulu!")
      print("Ketik 1 untuk membuka halaman login")
      print("ketik 7 untuk membuka home")
      user = str(input(nav))
    else:
      # FORM REGISTRASI
      namakend = str(input("Nama Kendaraan: "))
      tahunkend = str(input("Tahun Kendaraan: "))
      alamatkend = str(input("Alamat Kendaraan: "))
      hargakend = int(input("Harga sewa per hari: "))
      deskripsikend = str(input("Masukan Deskripsi Kendaraan: "))
      DB.navigateDatabase("insert into kendaraan (username,namakendaraan,tahun,alamat,harga,deskripsi) values ('{}','{}',{},'{}',{},'{}');".format(Akun.loginSession[0],namakend,tahunkend,alamatkend,hargakend,deskripsikend))
      print("Berhasil meregister kendaraan!")
      user = '3'