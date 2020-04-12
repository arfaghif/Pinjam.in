from Akun import *
class Command :
  def __init__(self, akun):
    self.akun = akun
    self.kendaraan = None
    self.obj = None
    self.fetchTransaksi = None
    self.transaksi = None
    self.penyewa = None
    self.query = None
    self.review = None

  def header(self):
    print("Selamat datang di Pinjam.in")
    if (self.akun.loginSession != None):
      print("Halo " + self.akun.loginSession[0])
      print("3. Lihat Kendaraan")
      print("4. Logout")
      print("5. Register Kendaraan")
      print("6. Daftar Transaksi")

      # Cek penyewa
      self.penyewa=[]
      self.akun.getDatabase().getData("select * from penyewa",self.penyewa)
      self.ispenyewa = 1
      for penyewa in self.penyewa:
        if (self.akun.loginSession[0] == penyewa[1]):
          self.ispenyewa = 0
      
      if (self.ispenyewa==0):
        print("8. Cari Kendaraan")
        print("Ketik 'konfirmasi' untuk Konfirmasi Penyewaan")
      else:
        print("7. Daftar menjadi Penyewa")
        print("8. Cari Kendaraan")
        print("9. Beri Ulasan")
      
      
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
      print("{}. {} tahun {} daerah {} sewa/hari {} by {}".format(nolist, kend[2], kend[3], kend[4], kend[5],kend[1]))
        
  def pilihKendaraan(self,index):
    self.review=[]
    self.obj = {'IDKend':self.kendaraan[index][0],'username':self.kendaraan[index][1],'nama':self.kendaraan[index][2],'tahun':self.kendaraan[index][3],'alamat':self.kendaraan[index][4],'harga':self.kendaraan[index][5],'deskripsi':self.kendaraan[index][6],'tersedia':self.kendaraan[index][7],'tambahan':self.kendaraan[index][8]}      
    self.akun.getDatabase().getData("select * from ulasan natural join kendaraan where IDKend={};".format(self.obj['IDKend']),self.review)
    print("")
    print("{} tahun: {} harga sewa/hari: {} alamat: {} deskripsi: {} by {}".format(self.obj['nama'],self.obj['tahun'],self.obj['harga'],self.obj['alamat'],self.obj['deskripsi'],self.obj['username']))
    if (self.obj['tersedia']=='y'):
      print("Tersedia supir: Ya, tambahan sewa supir (dalam persen harga sewa): {}".format(self.obj['tambahan']))
    else:
      print("Tersedia supir: Tidak")
    print('')
    print("Ulasan dari pengguna/customer: ")
    if (len(self.review)==0):
      print("Belum ada ulasan")
    for ulasan in self.review:
      print("Ulasan dari {}: {}".format(ulasan[2], ulasan[3]))
    print("")
    # Dapat memilih opsi kontak atau kembali ke home setelah pada page kendaraan

  def regisKendaraan(self):
    namakend = str(input("Nama Kendaraan: "))
    tahunkend = str(input("Tahun Kendaraan: "))
    alamatkend = str(input("Alamat Kendaraan: "))
    hargakend = int(input("Harga sewa per hari: "))
    deskripsikend = str(input("Masukan Deskripsi Kendaraan: "))
    tersediasupir = str(input("Tersedia supir? Y/N: "))
    tersediasupir=tersediasupir.lower()
    if tersediasupir=='y':
      tambahansupir = input("Berapa sewa tambahan supir(dalam persen harga sewa): ")
      self.akun.getDatabase().navigateDatabase("insert into kendaraan (username,namakendaraan,tahun,alamat,harga,deskripsi,tersediasupir,tambahan) values ('{}','{}',{},'{}',{},'{}','{}',{});".format(self.akun.loginSession[0],namakend,tahunkend,alamatkend,hargakend,deskripsikend,tersediasupir, tambahansupir))
    else:
      self.akun.getDatabase().navigateDatabase("insert into kendaraan (username,namakendaraan,tahun,alamat,harga,deskripsi,tersediasupir,tambahan) values ('{}','{}',{},'{}',{},'{}','{}',{});".format(self.akun.loginSession[0],namakend,tahunkend,alamatkend,hargakend,deskripsikend,tersediasupir, 0))
    print("Berhasil meregister kendaraan!")

  def jadiPenyewa(self):
    self.akun.getDatabase().navigateDatabase("insert into penyewa (username) values ('{}')".format(self.akun.loginSession[0]))
    print("")
    print("Berhasil menjadi penyewa!")
    print("")

  def tampilkanKontak(self):
    kontakCurrent=[]
    self.akun.getDatabase().getData("Select email,no_hp from kontak natural join akun where username='{}'".format(self.obj['username']), kontakCurrent)
    print("Kontak Pemilik: ")
    print("email: {}".format(kontakCurrent[0][0]))
    print("no hp: {}".format(kontakCurrent[0][1]))

  def nominalPenawaran(self):
    penawaran=None
    unamepenyewa=None
    existTransaksi = False
    self.fetchTransaksi = []
    konfirmasi = 0
    status = 'PENDING'
    # CEK Transaksi sudah ada
    self.akun.getDatabase().getData("select * from transaksi",self.fetchTransaksi)
    for transaksi in self.fetchTransaksi:
      if (transaksi[1]==self.obj["IDKend"] and transaksi[3]==self.obj["username"] and transaksi[4]==self.akun.loginSession[0] and (transaksi[5]==0 or (transaksi[5]==1 and transaksi[6]=="DITERIMA"))):
        existTransaksi = True
    
    # Bila transaksi tidak ada
    if not (existTransaksi):
      nominal = int(input())
      self.akun.getDatabase().navigateDatabase("insert into transaksi (IDKend,nominal,unamepenyewa,unamepembeli,konfirmasi,status) values ({},{},'{}','{}',{},'{}')".format(self.obj["IDKend"],nominal,self.obj["username"],self.akun.loginSession[0],konfirmasi,status))
      print("Berhasil di Ajukan!")
    else:
      print("Transaksi sedang menunggu konfirmasi! / Sudah Di Terima!")
  
  def daftarTransaksi(self):
    # Inisiasi Variabel dan Fetch Record
    self.transaksi=[]
    self.akun.getDatabase().getData("select unamepenyewa,unamepembeli,nominal,konfirmasi,status,namakendaraan,IDTransaksi from transaksi natural join kendaraan;",self.transaksi)
    # print(self.transaksi)
    
    # Get Record Daftar Transaksi
    print("")
    print("DAFTAR TRANSAKSI: ")
    for trans in self.transaksi:
      if (trans[self.ispenyewa]==self.akun.loginSession[0]):
        if (trans[3]==1 and self.ispenyewa==1):
          print("No Trans: {}, Penyewa: {}, Nominal: {}, Konfirmasi: sudah, Status: {}, Nama Kendaraan: {}".format(trans[6],trans[0], trans[2], trans[4], trans[5]) )
        elif (trans[3]==0 and self.ispenyewa==1):
          print("No Trans: {}, Penyewa: {}, Nominal: {}, Konfirmasi: belum, Status: {}, Nama Kendaraan: {}".format(trans[6],trans[0], trans[2], trans[4], trans[5]) )
        elif (trans[3]==1 and self.ispenyewa==0):
          print("No Trans: {}, Pembeli: {}, Nominal: {}, Konfirmasi: sudah, Status: {}, Nama Kendaraan: {}".format(trans[6],trans[1], trans[2], trans[4], trans[5]) )
        elif (trans[3]==0 and self.ispenyewa==0):
          print("No Trans: {}, Pembeli: {}, Nominal: {}, Konfirmasi: belum, Status: {}, Nama Kendaraan: {}".format(trans[6],trans[1], trans[2], trans[4], trans[5]) )
    print("")
  
  def cariKendaraan(self):   
    exist=True 
    self.kendaraan=[]
    self.query=[]
    print("Pilihan Kendaraan:")
    self.akun.getDatabase().getData("Select * from kendaraan", self.kendaraan)
    
    objIndex={
      'namakendaraan': 2,
      'tahun': 3,
      'alamat': 4,
      'harga': 5
    }

    print("Pilih salah satu indikator pencarian dan ketik indikator tersebut: ")
    searchparam=input("berdasarkan? [namakendaraan] [tahun] [alamat] [harga]: ")
    if searchparam=='harga' or searchparam=='tahun':
      upordown=input("diatas range? atau di bawah? format [atas] [bawah]: ")
      search=input(searchparam + " tersebut: ")
      if (upordown=='atas'):
        for kend in self.kendaraan:          
          if (int(search)<kend[objIndex[searchparam]]):
            self.query.append(kend)
      else:
        for kend in self.kendaraan:          
          if (int(search)>kend[objIndex[searchparam]]):
            self.query.append(kend)
    else:
      search=input(searchparam + " tersebut: ")
      for kend in self.kendaraan:
        if (search==kend[objIndex[searchparam]]):
          self.query.append(kend)
      
    print("")
    print("Hasil pencarian: ")    
    
    if (len(self.query)==0):
      print("Tidak ada pencarian yang cocok")
      exist=False
      print(exist)
      print(len(self.query))    
    
    for nolist,query in enumerate(self.query,start=1):
      print("{}. {} tahun {} daerah {} sewa/hari {} by {}".format(nolist, query[2], query[3], query[4], query[5], query[1]))    
    print("")
    return exist

  def konfirmasiPenawaran(self):
    # Inisiasi Variabel dan Fetch Record
    tidakadatransaksi=False
    self.transaksi=[]
    self.akun.getDatabase().getData("select unamepenyewa,unamepembeli,nominal,konfirmasi,status,namakendaraan,IDTransaksi from transaksi natural join kendaraan;",self.transaksi)
    
    print("")
    print("Konfirmasikan: ")
    if (len(self.transaksi)==1):
      print("Belum ada transaksi yang harus di  konfirmasi")
      tidakadatransaksi=True
    else:
      for trans in self.transaksi:
        if (trans[self.ispenyewa]==self.akun.loginSession[0]):
          if (trans[3]==0 and self.ispenyewa==0):
            print("No Trans: {}, Pembeli: {}, Nominal: {}, Konfirmasi: belum, Status: {}, Nama Kendaraan: {}".format(trans[6],trans[1], trans[2], trans[4], trans[5]) )
      print("")

    if not (tidakadatransaksi):
      print("ketik 'exit' untuk membatalkan, ketik 'konfirmasi' untuk melanjutkan")
      lanjut = input()
      if (lanjut=='exit'):
        print("") 
      else:
        notransaksi = input("Masukan No Trans yang ingin di konfirmasi: ")
        print("A. terima, B. tolak")
        statusbaru = str(input())
        if (statusbaru=='A'):
          self.akun.getDatabase().navigateDatabase("UPDATE transaksi set status='DITERIMA', konfirmasi=1 where IDTransaksi={}".format(notransaksi))
          print("")
          print("Transaksi di terima")
          print("")
        else:
          self.akun.getDatabase().navigateDatabase("UPDATE transaksi set status='DITOLAK', konfirmasi=1 where IDTransaksi={}".format(notransaksi))
          print("")
          print("Transaksi di tolak")
          print("")
    
  def beriUlasan(self):
    if (self.ispenyewa==1):
      self.transaksi=[]
      self.akun.getDatabase().getData("select unamepenyewa,unamepembeli,nominal,konfirmasi,status,namakendaraan,IDTransaksi,IDKend from transaksi natural join kendaraan where unamepembeli='{}';".format(self.akun.loginSession[0]),self.transaksi)
      print("")
      if (len(self.transaksi)==0):
        print("Belum pernah transaksi")
        print("")
      else:
        for notrans,trans in enumerate(self.transaksi,start=1):
          if (trans[4]=='DITERIMA'):
            print("No Ulasan: {}, No Trans: {}, Penyewa: {}, Nominal: {}, Konfirmasi: sudah, Status: {}, Nama Kendaraan: {}".format(notrans,trans[6],trans[0], trans[2], trans[4], trans[5]) )
        print("")
        getNoUlasan=int(input("Masukan no kendaraan yang akan di ulas: "))
        review = input("Masukan ulasan anda: ")
        self.akun.getDatabase().navigateDatabase("insert into ulasan (IDKend, unamepembeli, review) values ({},'{}','{}');".format(self.transaksi[getNoUlasan-1][7],self.akun.loginSession[0],review))
        print("Berhasil menambahkan review")
        print("")
    



    