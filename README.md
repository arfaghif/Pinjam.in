# Aplikasi Sewa Menyewa Kendaraan - Pinjam.in
### author : Kelompok 7 K3 - Raja Skuy Living
### ditujukan kepada klien : Sekar Larasati Muslimah - 13517114

## Apa Pinjam.in itu ?
Pinjam.in adalah salah satu aplikasi yang menyediakan tempat untuk sewa menyewa kendaraan. 
Pinjam.in memfasilitasi orang-orang yang tidak memiliki kendaraan, namun ingin menggunakan kendaraan, dan orang-orang yang memiliki kendaraan, namun tidak sedang digunakan dan ingin disewakan.
Pinjam.in diambil dari kata "Pinjam" dan imbuhan "in" yang jika digabungkan bermakna meminjamkan.
Kendaraan yang dapat disewa dan disewakan pada aplikasi ini adalah mobil dan motor.

## Bagaimana cara menjalankan Pinjam.in ?
- Prasyarat : sudah terinstall MySql dan Python
- Setup :
1. Membuat database kosong pada MySql dengan mengetikkan `Create Database [nama database]` pada terminal MySql
2. Import 'database.sql' dari folder 'db' ke MySql dengan cara mengetikkan `Mysql -u root -p [nama database] < database.sql`
3. Buka file 'main.py' dan ubah kode program pada bagian 'db' menjadi `db = DB.DB([password mysql], [nama database])`
- Run :
1. Buka terminal dan jalankan main program dengan mengetikkan `python main.py`
2. Program akan membuka halaman utama
3. Selamat meminjam!

## Bagaimana cara meminjam ?
1. Pengguna harus Login terlebih dahulu untuk meminjam
2. Jika belum memiliki akun, maka lakukan Registrasi terlebih dahulu
3. Isi data pribadi dengan benar
!PERINGATAN! : Masukkan data pribadi dengan benar, terutama pada bagian tanggal lahir. Masukkan dengan format "YYYY-MM-DD"
4. Pengguna akan dialihkan ke halaman pencarian untuk memilih kendaraan
5. Jika ingin meminjam, klik pada pilihan kendaraan lalu klik Pinjam
6. Pengguna diminta untuk memasukkan berapa hari kendaraan akan dipinjam
7. Pengguna akan ditawarkan ingin menyewakan supir atau tidak
7. Selanjutnya pengguna diminta untuk membayar biaya sewa dengan cara memasukkan ID transaksi dan biaya sewa yang sesuai
8. Selamat kendaraan telah berhasil dipinjam!

## Bagaimana cara menyewakan ?
1. Pengguna yang ingin menyewakan harus mendaftarkan diri sebagai peminjam
2. Pendaftaran peminjam dapat dilakukan dengan cara meng-klik pilihan menjadi Penyewa
3. Peminjam dapat mendaftarkan kendaraan
!PERINGATAN! : Masukkan data kendaraan dengan benar. Memasukkan data kendaraan yang salah akan berakibat aplikasi menjadi error

### Keterangan
Aplikasi ini sangat sederhana, namun berpotensi untuk dikembangkan menjadi aplikasi yang siap digunakan masyarakat luas
Karena aplikasi ini masih sederhana, maka aplikasi ini memiliki beberapa bug. Untuk menghindari bug tersebut, maka ikutilah tata cara penggunaan dengan benar
Terimakasih! Selamat menyewa dengan Pinjam.in!