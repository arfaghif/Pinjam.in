import pytest 
from command import * 
from faker import Faker

# Akun set test
dB = DB("afterlife86","rpl")
akun=Akun(dB)
command = Command(akun)
fake = Faker() 

# Pada test kali ini, data di generate untuk selalu random pada setiap running nya 


class TestClass():
    def test_login(self):
        # Data login
        login_data=[]

        # Fetch data akun, dan login
        akun.getDatabase().getData("select * from akun where username='pals'", login_data)
        akun.login(login_data[0][0],login_data[0][1])
        
        # test login session dengan akun yang di login 
        assert akun.loginSession[0] == login_data[0][0]
        assert akun.loginSession[1] == login_data[0][1]

        # exit
        akun.logout()

    def test_register(self):
        # register random username dan password
        username1=fake.name().replace(" ", "").lower()
        password1=fake.name().replace(" ", "").lower()
        
        # melakukan register
        akun.register(username1, password1)

        # bila register berhasil, login session menjadi akun baru
        assert akun.loginSession[0] == username1
        assert akun.loginSession[1] == password1

    def test_regis_penyewa(self):
        penyewa=[]
        command.jadiPenyewa()
        akun.getDatabase().getData('select * from penyewa', penyewa)
        for unamepenyewa in penyewa:
            # menjadi penyewa
            if (unamepenyewa[1]==akun.loginSession[1]):
                # assert untuk keberhasilan login
                assert unamepenyewa[1]==akun.loginSession[1]

    def test_transaksi(self):
        # membuat daftar transaksi
        transaksiAssert=[]
        akun.getDatabase().navigateDatabase("insert into transaksi (IDKend,nominal,unamepenyewa,unamepembeli,konfirmasi,status) values ({},{},'{}','{}',{},'{}')".format(6,20000,"ibnu",akun.loginSession[0],0,"PENDING"))
        akun.getDatabase().getData("select * from transaksi where unamepembeli='{}'".format(akun.loginSession[0]) , transaksiAssert)
        
        # Data random akan sama dengan data transaksi yang telah di record
        assert transaksiAssert[0][4] == akun.loginSession[0]
        
    def test_konfirmasi_transaksi(self):
        konfirmasiAssert=[]
        # Konfirmasi Transaksi Penyewa
        akun.getDatabase().navigateDatabase("update transaksi set status='DITERIMA' where unamepembeli='{}'".format(akun.loginSession[0]))

        # Mencari transaksi pembeli
        akun.getDatabase().getData("select * from transaksi where unamepembeli='{}'".format(akun.loginSession[0]) , konfirmasiAssert)

        # Test untuk transaksi ketika berhasil di konfirmasi (data record di update)
        assert konfirmasiAssert[0][6] == 'DITERIMA'

    def test_ulasan(self):
        getIDKend = []
        getTestReview = []
        akun.getDatabase().getData("select IDKend from transaksi where unamepembeli='{}'".format(akun.loginSession[0]),getIDKend)
        review = 'test review'
        akun.getDatabase().navigateDatabase("insert into ulasan (IDKend, unamepembeli, review) values ({},'{}','{}');".format(getIDKend[0][0],akun.loginSession[0],review))
        akun.getDatabase().getData("select * from ulasan where unamepembeli='{}' and IDKend={};".format(akun.loginSession[0], getIDKend[0][0]), getTestReview)
        
        # ulasan untuk data record random 
        assert getTestReview[0][3] == review

    def test_regis_kendaraan(self):
        getRegisKendaraan=[]
        akun.getDatabase().navigateDatabase("insert into kendaraan (username,namakendaraan,tahun,alamat,harga,deskripsi,tersediasupir,tambahan) values ('{}','{}',{},'{}',{},'{}','{}',{});".format(akun.loginSession[0],'namakend',2000,'alamatkend',1000,'deskripsikend','y', 5))
        akun.getDatabase().getData("select * from kendaraan where username='{}'".format(akun.loginSession[0]), getRegisKendaraan)

        # kendaraan yang di record user random akan sama
        assert getRegisKendaraan[0][1] == akun.loginSession[0]

