# Pertemuan11
Nama  : Muhammad Shiddiq<br>
Kelas : TI.22.B1<br>
Nim   : 312210125<br>

# Tugas ini dibuat untuk menyelesaikan latihan dan praktikum 6

Latihan 
1. Pertama buat folder untuk mengerjakan latihan.py dan praktikum 6.py

![NamaFolder(11)](https://user-images.githubusercontent.com/115475520/205484101-2346bf88-8371-4bfb-b8ef-56646d95f9d6.png)

2. Kemudian masuk pada file latihan.py dan masukkan program seperti ini.
```import math 

def a(x) :
    return x**2

def b(x, y):
    return math.sqrt(x**2 + y**2)

def c(*args):
    return sum(args)/len(args)

def d(S):
    return "".join(set(s))
```

![Screenshot (78)](https://user-images.githubusercontent.com/115475520/205485934-a5896c35-44e0-4c91-9dc9-20fbba8b2564.png)

3. Selanjutnya kita pindah ke praktikum 6, buka file praktikum6.py 

![NamaFolder(11)](https://user-images.githubusercontent.com/115475520/205484101-2346bf88-8371-4bfb-b8ef-56646d95f9d6.png)

4. Kemudian masukkan program sebagai berikut.
```
from tabulate import tabulate

# Buat dictionary yang memiliki value berupa list
data = {'nama' : [], 'nilai': [] }

def tampilkan():
       # variabel i untuk membuat penomoran data ketika dibuat tabel
       i = range(1, len(data['nama'])+1)
       # membuat list header kolom yang akan ditampilkan
       headers = ["No", "Nama", "Nilai"]

       # data dapat ditampilkan jika variabel data terisi minimal satu data
       if len(data['nama']) > 0:
           print(tabulate(data, headers, showindex=i,tablefmt="rounded_outline"))

       # jika tidak ada data, maka tampilkan pesan
       else:
           print("\nTidak Ada Data \n")


def tambah():
       # buat inputan untuk mengisi nim
       nama = input("Masukkan Nama : ")

       # jika nim yang di input tersedia pada variabel data, cetak pesan lalu lakukan input ulang
       while nama in data['nama']:
           print("Mahasiswa dengan nama yang sama sudah ada")
           nama = input("Masukkan Nama : ")

       nilai = input("masukkan nilai : ")
       while not nilai.isnumeric():
           nilai = input("masukkan nilai : ")

       data['nama'].append(nama)
       data['nilai'].append(int(nilai))
       print("Data Berhasil Ditambah!!")


def hapus(nama):
       if nama in data['nama']:
           # buat dictionary kosong untuk menampilkan data yang cocok sesuai input NIM
           dataMhs = {}
           index = data['nama'].index(nama)

           # lakukan pengisian data yang cocok ke dalam variabel dataMhs
           for key in data.keys():
               dataMhs[key] = []
               dataMhs[key].append(data[key][index])
           print(tabulate(dataMhs, headers="keys", tablefmt="rounded_outline"))
           # lakukan konfirmasi penghapusan
           confirm = input("anda yakin ingin menghapus data ini?? (y/t)")

           # jika input selain y atau t lakukan konfirmasi berulang
           while (confirm not in ['y', 't']):
               print("input salah")
               confirm = input("anda yakin ingin menghapus data ini?? (y/t)")

           # jika konfirmasi selesai dilakukan, maka hapus data mahasiswa pada variabel data
           if confirm == "y":
               for key in data.keys():
                   data[key].pop(index)
               print("Data Berhasil Dihapus!!\n")

       else:
           print("data nama tidak ditemukan!!")


def ubah(nama):
       if nama in data['nama']:
           # buat dictionary kosong untuk menampilkan data yang cocok sesuai input nama
           dataMhs = {}
           index = data['nama'].index(nama)
           # lakukan pengisian data yang cocok ke dalam variabel dataMhs
           for key in data.keys():
               dataMhs[key] = []
               dataMhs[key].append(data[key][index])

           print(tabulate(dataMhs, headers="keys", tablefmt="rounded_outline"))
           # lakukan input data apa yang akan diubah
           pilihan = input("pilih field yang akan diubah : \n1.Nama\n2.Nilai\n")
           # lakukan pengecekan pada variabel pilihan yang dikonversi menjadi nilai integer
           match int(pilihan):
               case 1:
                   print("data nama sebelumnya : " + dataMhs['nama'][0])
                   nama = input("Masukkan nama Baru : ")
                   while nama in data['nama']:
                       if nama == dataMhs['nama'][0]:
                           break
                       print("Mahasiswa dengan nama yang sama sudah ada")
                       nama = input("Masukkan nama Baru : ")
                   data['nama'][index] = nama

               case 2:
                   print("data nilai sebelumnya :" , dataMhs['nilai'][0])
                   nilai = input("Masukkan nilai baru : ")
                   data['nilai'][index] = nilai

           for key in data.keys():
               dataMhs[key] = []
               dataMhs[key].append(data[key][index])
           print(tabulate(dataMhs, headers="keys", tablefmt="rounded_outline"))

       else:
           print("data nama tidak ditemukan!")

       while True:
            print("[ (l)ihat , (t)ambah, (u)bah, (h)apus, (k)eluar ] \n")
            tanya = input("Masukkan Pilihan : ")
            match tanya:
                case "l":
                    tampilkan()
                case "t":
                    tambah()
                case "u":
                    tampilkan()
                    if len(data['nama']) > 0:
                        nama = input("masukkan nama siswa yang akan diubah : ")
                        ubah(nama)
                case "h":
                    tampilkan()
                    if len(data['nama']) > 0:
                        nama = input("masukkan nama siswa yang akan dihapus : ")
                        hapus(nama)
                case "k":
                    print("anda sudah Keluar dari program")
                    break
                case _:
                    print("Tidak Sesuai Pilihan, Silahkan Pilih Kembali!!\n")
                    continue
```
# Terima Kasih mohon maaf jika ada kesalahan.
