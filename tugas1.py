'''
Nama: Dani Mahardika Suroso
NIM: 205150301111012

Contoh program ceklist barang dengan menggunakan tipe data List
'''

Judul = input('Masukkan judul checklist: ')
NamaList = []
while True:
    nama = input('Masukkan item ke ' + str(len(NamaList) + 1) +
    ' (Atau tekan enter jika sudah selesai):')
    if nama == '':
        break
    NamaList = NamaList + [nama]
print('List item Anda adalah:')
ListCentang = []
ListUncheck = []
for i in NamaList:
    pilihan = input('Centang item ' + i + ' (Ya/Tidak) ')
    if pilihan == 'Ya' or pilihan == 'ya':
        ListCentang.append("Ya")
        print(ListCentang)
    else:
        ListUncheck.append("Tidak")
x = ListCentang.count("Ya")
y = ListUncheck.count("Tidak")
print('Jumlah item yang telah dicentang: ' + str(x))
print('Jumlah item yang tidak dicentang: ' + str(y))